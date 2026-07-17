import Foundation
import AVFoundation

let args = CommandLine.arguments
guard args.count >= 3 else { FileHandle.standardError.write("usage: tonemap <in> <out>\n".data(using:.utf8)!); exit(64) }
let inURL = URL(fileURLWithPath: args[1])
let outURL = URL(fileURLWithPath: args[2])
try? FileManager.default.removeItem(at: outURL)

let asset = AVURLAsset(url: inURL)
let sem = DispatchSemaphore(value: 0)
var code: Int32 = 0

AVMutableVideoComposition.videoComposition(withPropertiesOf: asset) { comp, err in
    guard let comp = comp else {
        print("videoComposition error: \(String(describing: err))"); code = 2; sem.signal(); return
    }
    // Force SDR Rec.709 output tags -> AVFoundation tone-maps the HLG/BT.2020 source.
    comp.colorPrimaries = AVVideoColorPrimaries_ITU_R_709_2
    comp.colorTransferFunction = AVVideoTransferFunction_ITU_R_709_2
    comp.colorYCbCrMatrix = AVVideoYCbCrMatrix_ITU_R_709_2

    guard let export = AVAssetExportSession(asset: asset, presetName: AVAssetExportPresetHighestQuality) else {
        print("no export session"); code = 3; sem.signal(); return
    }
    export.outputURL = outURL
    export.outputFileType = .mov
    export.videoComposition = comp
    export.exportAsynchronously {
        switch export.status {
        case .completed: print("OK")
        default: print("export failed: \(String(describing: export.error))"); code = 4
        }
        sem.signal()
    }
}
sem.wait()
exit(code)
