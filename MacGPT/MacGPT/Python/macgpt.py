import Foundation
import PythonKit

class PythonBridge: NSObject {
    private let python = Python.shared

    override init() {
        super.init()
        guard let pythonPath = Bundle.main.path(forResource: "macgpt", ofType: "py") else {
            print("Error: Failed to locate macgpt.py")
            return
        }

        // Load the Python script
        python.run(scriptPath: pythonPath)
    }

    func sendMessage(_ message: String) {
        // Call the Python function to send a message
    }

    // Add other necessary functions to interact with the Python script
}

