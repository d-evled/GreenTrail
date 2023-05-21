//
//  RedOneView.swift
//  TabView
//
//  Created by Sam Xie on 5/20/23.
//

import MapKit
import SwiftUI

struct MapView: View {
    @StateObject private var viewModel = ContentViewModel()
    
    var body: some View {
        Map(coordinateRegion: $viewModel.region, showsUserLocation: true)
            .edgesIgnoringSafeArea(.top)
            .accentColor(Color(.systemIndigo))
            .onAppear(){
                viewModel.checkIfLocationServiceIsEnabled()
            }
    }
    
}

struct MapView_Previews: PreviewProvider {
    static var previews: some View {
        MapView()
    }
}

