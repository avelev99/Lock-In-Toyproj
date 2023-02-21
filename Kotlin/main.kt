import java.awt.AWTException;
import java.awt.Rectangle;
import java.awt.Robot;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import org.opencv.core.Core;
import org.opencv.core.CvType;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Scalar;
import org.opencv.imgcodecs.Imgcodecs;
import org.opencv.imgproc.Imgproc;

public class Main {
    static { System.loadLibrary(Core.NATIVE_LIBRARY_NAME); }

    public static boolean clickImage(String imageFile, double threshold) {
        Mat sourceImage =
            Imgcodecs.imread(imageFile, Imgcodecs.IMREAD_GRAYSCALE);
        Mat screenshot = null;
        try {
            BufferedImage screenFullImage =
                new Robot().createScreenCapture(new Rectangle(
                    java.awt.Toolkit.getDefaultToolkit().getScreenSize()));
            screenshot = new Mat(screenFullImage.getHeight(),
                                screenFullImage.getWidth(), CvType.CV_8UC3);
            screenshot.put(
                0, 0,
                ((DataBufferByte)screenFullImage.getRaster().getDataBuffer())
                    .getData());
            Imgproc.cvtColor(screenshot, screenshot, Imgproc.COLOR_BGR2GRAY);
        } catch (AWTException e) {
            e.printStackTrace();
        }

        Mat result = new Mat();
        Imgproc.matchTemplate(screenshot, sourceImage, result,
                                Imgproc.TM_CCOEFF_NORMED);
        Point minLoc = new Point();
        Point maxLoc = new Point();
        Core.MinMaxLocResult mmr = Core.minMaxLoc(result);
        maxLoc = mmr.maxLoc;

        if (mmr.maxVal >= threshold) {
            Point bottomRight = new Point(maxLoc.x + sourceImage.cols(),
                                            maxLoc.y + sourceImage.rows());
            Point center = new Point((bottomRight.x - maxLoc.x) / 2 + maxLoc.x,
                                        (bottomRight.y - maxLoc.y) / 2 + maxLoc.y);

            try {
                Robot robot = new Robot();
                robot.mouseMove((int)center.x, (int)center.y);
                robot.mousePress(java.awt.event.InputEvent.BUTTON1_DOWN_MASK);
                robot.mouseRelease(java.awt.event.InputEvent.BUTTON1_DOWN_MASK);
            } catch (AWTException e) {
                e.printStackTrace();
            }

            return true;
        }

        return false;
    }

    public static void runDetectionAndClickingLoop(String imageFile) {
        while (true) {
            boolean isImageFound = clickImage(imageFile, threshold);
            if (!isImageFound) {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            } else {
                break;
            }
        }
    }

    public static void championPickAndBan(String championName) {
        runDetectionAndClickingLoop("Search.png");
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Type the champion name
        // Fill in appropriate method to type the champion name

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        // Click on the screen at (962, 454)
        // Fill in appropriate method to click on the screen at (962, 454)
    }

    public static void startGame() {
        boolean searchFlag = false;
        while (true) {
            if (!searchFlag) {
                boolean isSearchFound = clickImage("Search.png", threshold);
                if (isSearchFound) {
                    searchFlag = true;
                    break;
                }
            } else {
                boolean isAcceptFound = clickImage("Accept.png", threshold);
                if (isAcceptFound) {
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        startGame();

        // Call championPickAndBan with the champion_name variable
        // Fill in appropriate method to call championPickAndBan with the
        // champion_name variable

        runDetectionAndClickingLoop("Ban_Inactive.png");

        // Call championPickAndBan with the ban_name variable
        // Fill in appropriate method to call championPickAndBan with the
        // ban_name variable

        runDetectionAndClickingLoop("Ban_Active.png");
        runDetectionAndClickingLoop("Lock_In.png");
    }
}
while (true) {
    boolean result = clickImage(imageFile, 0.9);
    if (result) {
        break;
    } else {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}