from strsimpy.cosine import Cosine


cosine=Cosine(3)

def get_matched_row_grade_metrics(struct: dict)->float:
    grade_field1=cosine.similarity(struct['field1'], struct['disturbed_field1'])
    grade_field2=cosine.similarity(struct['field2'], struct['disturbed_field2'])
    grade_field3=cosine.similarity(struct['field3'], struct['disturbed_field3'])
    grade=(grade_field1+grade_field2+grade_field3)/3
    return grade