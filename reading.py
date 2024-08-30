import cv2

##reading an image
def show_img():
    image = cv2.imread("image_trial.jpg", cv2.IMREAD_UNCHANGED)
    image = cv2.flip(image, 1) ##flips the image vertically
    image = cv2.resize(image, (0, 0), fx = 0.25, fy = 0.25)##scales the image to 1/4 its original size
    
    cv2.rectangle(image, (10, 10), (500, 50), (255, 0, 0), 2, 1)##Drawing a rectangle
    cv2.circle(image, (int(image.shape[1]/2), int(image.shape[0]/2)), 50, (0, 0, 0), 4)##drawing a circle
    cv2.imshow("", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_vid():
    vid = cv2.VideoCapture("vid1.mp4")

    while True:
        ret, frame = vid.read()

        if ret == False or cv2.waitKey(1) == ord("q"):
            break
        else:
            frame = cv2.flip(frame, 1)
            frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5)
            cv2.imshow("", frame)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_img()