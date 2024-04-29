import cv2
import asyncio


async def capture_frames():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        await asyncio.sleep(0.01)

    cap.release()
    cv2.destroyAllWindows()


async def main():
    await capture_frames()


if __name__ == '__main__':
    asyncio.run(main())
