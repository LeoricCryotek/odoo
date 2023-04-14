//
//  AppDelegate.swift
//  MacGPT
//
//  Created by Daniel Santiago on 4/14/23.
//
import Cocoa

@main
class AppDelegate: NSObject, NSApplicationDelegate {

    func applicationDidFinishLaunching(_ notification: Notification) {
        
        createAppFolders()
        
        // Override point for customization after application launch.
    }
    
    // Other AppDelegate methods...

    func createAppFolders() {
        let fileManager = FileManager.default

        guard let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first else {
            print("Error: Unable to find Documents folder.")
            return
        }

        let macGPTFolder = documentsURL.appendingPathComponent("MacGPT")
        let resourcesFolder = macGPTFolder.appendingPathComponent("Resources")

        do {
            try fileManager.createDirectory(at: macGPTFolder, withIntermediateDirectories: true, attributes: nil)
            try fileManager.createDirectory(at: resourcesFolder, withIntermediateDirectories: true, attributes: nil)
        } catch {
            print("Error: Unable to create directories: \(error)")
        }
    }
}
