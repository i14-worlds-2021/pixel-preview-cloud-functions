
import main
import os

def test_process_image():
    bucket_name = 'i14-worlds-2021-upload'
    src_file_name = 'AC75AmericanMagic_d41dbb268a/Int-14-Day-7-5.jpg'
    main.process_image(bucket_name, src_file_name)


if __name__ == '__main__':

    # Put the service-account.json within the same directory!
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service-account.json"
    test_process_image()