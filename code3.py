import code2

PEOPLE_PER_SQUARE_METER = 2
FIELD_LENGTH = 60
FIELD_WIDTH = 45
people_at_concert = (
    code2.rectangle(FIELD_LENGTH, FIELD_WIDTH) * PEOPLE_PER_SQUARE_METER
)
print("estão presentes no show aproximadamente", people_at_concert)