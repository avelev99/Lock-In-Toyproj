package main

import (
	"fmt"
	"image"
	"image/png"
	"os"
	"time"

	"github.com/getlantern/systray"
	"github.com/skratchdot/open-golang/open"
	"github.com/go-vgo/robotgo"
)

const (
	acceptImageFile   = "Accept.png"
	searchImageFile   = "Search.png"
	banInactiveFile   = "Ban_Inactive.png"
	banActiveFile     = "Ban_Active.png"
	lockInImageFile   = "Lock_In.png"
	//searchString asks the user to input a string to search for
	
	mordeSearchString  = "Morde"
	dariusSearchString = "Darius"
)

func main() {
	systray.Run(onReady)
}

func onReady() {
	systray.SetIcon(getIcon("icon.png"))
	systray.SetTitle("My App")
	systray.SetTooltip("My App")

	mQuitOrig := systray.AddMenuItem("Quit", "Quit the whole app")
	go func() {
		<-mQuitOrig.ClickedCh
		fmt.Println("Requesting quit")
		systray.Quit()
		fmt.Println("Finished quitting")
	}()

	systray.AddMenuItem("Open App", "Open the app").SetIcon(getIcon("folder.png"))

	for {
		// Check for the "Accept" image continuously
		if imageExists(acceptImageFile) {
			// Click on the "Accept" image
			clickImage(acceptImageFile)

			// Check for the other images only once
			if imageExists(searchImageFile) {
				clickImage(searchImageFile)
				typeString(mordeSearchString)
			}
			if imageExists(banInactiveFile) {
				clickImage(banInactiveFile)
				clickImage(searchImageFile)
				typeString(dariusSearchString)
			}
			if imageExists(banActiveFile) {
				clickImage(banActiveFile)
			}
			if imageExists(lockInImageFile) {
				clickImage(lockInImageFile)
			}
		}
		time.Sleep(500 * time.Millisecond)
	}
}

func getIcon(iconFile string) []byte {
	// Open the icon file
	iconFileHandle, err := os.Open(iconFile)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	defer iconFileHandle.Close()

	// Decode the icon file
	icon, err := png.Decode(iconFileHandle)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	// Encode the icon to a byte slice
	iconBytes, err := png.Encode(iconBytes, icon)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}

	return iconBytes
}

func imageExists(imageFile string) bool {
	// Open the image file
	imageFileHandle, err := os.Open(imageFile)
	if err != nil {
		return false
	}
	defer imageFileHandle.Close()

	// Check if the image file is valid
	_, err = png.Decode(imageFileHandle)
	if err != nil {
		return false
	}

	return true
}

func clickImage(imageFile string) {
	// Load the image file
	imageFileHandle, err := os.Open(imageFile)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer imageFileHandle.Close()

	// Decode the image file
	image, err := png.Decode(imageFileHandle)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Find the image on the screen
	x, y := robotgo.FindBitmap(image)
	if x == -1 || y == -1 {
		return
	}

	// Click on the image
	robotgo.MoveMouse(x, y)
	robotgo.MouseClick()
}

func typeString(s string) {
	// Type the string
	robotgo.TypeStr(s)
}