import face_recognition


def get_encoding(img):
    return face_recognition.face_encodings(img)


def mock(img):
    print(type(img))
    return img
