//
//  ContentView.swift
//  TabView
//
//  Created by Sam Xie on 5/20/23.
//

import SwiftUI

struct ContentView: View {
    @EnvironmentObject var vm: ViewModel
    var body: some View {
        TabView {
            MapView()
                .tabItem {
                    Image(systemName: "map")
                    Text("Bin Map")
                }
            CameraView()
//            MainView()
                .tabItem {
                    Image(systemName: "camera")
                    Text("Camera")
                }
//            GreenThreeView()
//                .tabItem {
//                    Image(systemName: "plus.square")
//                    Text("Add Bin")
//                }
            
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
            .environmentObject(ViewModel())
    }
}
