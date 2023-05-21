//
//  TabViewApp.swift
//  TabView
//
//  Created by Sam Xie on 5/20/23.
//

import SwiftUI

@main
struct TabViewApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
                .environmentObject(ViewModel())
                .onAppear {
                    UserDefaults.standard.setValue(false, forKey: "_UIConstraintBasedLayoutUnsatisfiable")
                }
        }
    }
}
