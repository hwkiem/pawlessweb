import face_recognition

def get_encoding(img):

    face_locations = face_recognition.face_locations(img)

    return face_recognition.face_encodings(img)


