//
//  BlueTwoView.swift
//  TabView
//
//  Created by Sam Xie on 5/20/23.
//

import SwiftUI
import UIKit
import CoreML
import Foundation

struct CameraView: View {
    @EnvironmentObject var vm: ViewModel
    var body: some View {
        var firstRun = true

        /// A predictor instance that uses Vision and Core ML to generate prediction strings from a photo.
        let imagePredictor = ImagePredictor()

        /// The largest number of predictions the main view controller displays the user.
        let predictionsToShow = 2
        NavigationView {
            VStack {
                if let imageX = vm.image {
                    Image(uiImage: imageX)
                        .resizable()
                        .scaledToFit()
                } else {
                    Image(systemName: "photo.fill")
                        .resizable()
                        .scaledToFit()
                        .opacity(0.6)
                        .frame(minWidth: 0, maxWidth: .infinity)
                        .padding(.horizontal)
                }
                HStack{
                    Button {
                        vm.source = .camera
                        vm.showPhotoPicker()
                    } label: {
                        Text("Camera")
                    }
                    Button {
                        vm.source = .library
                        vm.showPhotoPicker()
                    } label: {
                        Text("Photos")
                    }
//                    Button (action: MainViewController.mainView.userSelectedPhoto(<#T##UIImage#>)){
//
//                    } label: {
//                        Text("Predict")
//                    }
                }
                Spacer()
            }
            .sheet(isPresented: $vm.showPicker) {
                ImagePicker(sourceType: vm.source == .library ? .photoLibrary : .camera, selectedImage: $vm.image)
                    .ignoresSafeArea()
            }
            .alert("Error", isPresented: $vm.showCameraAlert, presenting: vm.cameraError, actions:
                    { cameraError in
                    cameraError.button
            }, message: { cameraError in
                Text(cameraError.message)
            })
            .navigationTitle("Image to Add")
        }
    }
}


struct CameraView_Previews: PreviewProvider {
    static var previews: some View {
        CameraView()
            .environmentObject(ViewModel())
    }
}
