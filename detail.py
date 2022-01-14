

from collections import Counter
import pickle
import underthesea
import wikipedia as wkp
wkp.set_lang("vi")


def word_tokenize(sent):
    words = underthesea.word_tokenize(sent)
    results = []
    for word in words:
        check = True
        for token in word.split():
            if not token.isalpha():
                check = False
                break
        if check:
            results.append(word)
    return results


def get_keywords(src, counter, threshold=0):
    result = {}
    word_list = []
    for sent in underthesea.sent_tokenize(src):
        word_list += word_tokenize(sent.lower())
    for word in set(word_list):
        count = counter[word]
        if count <= threshold:
            result[word] = count
    return result


def get_wiki_summary(keyword):
    summary = ''
    try:
        summary = wkp.summary(keyword)
    except:
        summary = ''
    return summary


with open('./data/word_counter_200k.pkl', 'rb') as file:
    COUNTER = pickle.load(file)


def get_detail(src, counter=COUNTER):
    result = {}
    for keyword in get_keywords(src, counter):
        result[keyword] = get_wiki_summary(keyword)
    return result


if __name__ == '__main__':
    src = '''Nền tảng khoa học
Thalassemia là một trong các bất thường di truyền theo kiểu lặn phổ biến nhất trên thế giới. Hiện có 7% người dân trên toàn cầu mang gen bệnh tan máu bẩm sinh; 1,1% cặp vợ chồng có nguy cơ sinh con bị bệnh hoặc mang gen bệnh. Bệnh có tỷ lệ cao ở vùng Địa Trung Hải, Trung Đông, châu Á - Thái Bình Dương trong đó Việt Nam là một trong những nước có tỷ lệ mắc bệnh và mang gen bệnh cao. Tại Việt Nam, tỷ lệ mang gen bệnh ở người Kinh vào khoảng 2 - 4%, các dân tộc thiểu số sống ở miền núi, tỷ lệ này rất cao: Khoảng 22% đối với dân tộc Mường, và trên 40% ở dân tộc Êđê , Tày, Thái và Siêng. Có 2 loại Thalassemia chính là Alpha Thalassemia và Beta Thalassemia. Beta thalassemia được gây ra bởi các đột biến trên gen HBB. Gen này mã hóa một protein của hemoglobin, liên quan đến vận chuyển oxy. Sự thiếu hụt của hemoglobin dẫn đến tình trạng thiếu máu đặc trưng của bệnh lý.
Beta-thalassemia có thể được phân thành ba kiểu thể chính:
Thể nhẹ, trong đó chỉ có một gen bị ảnh hưởng và nó không có triệu chứng.
Thể trung gian, biểu hiện các triệu chứng lâm sàng giữa nặng và nhẹ. Các dấu hiệu và triệu chứng của thalassemia thể trung gian thường biểu hiện sau hai tuổi và có thể bao gồm thiếu máu nhẹ đến trung bình, chậm lớn, mệt mỏi và dị dạng xương.
Thể nặng, còn được gọi là thiếu máu Cooley, trong đó cả hai gen đều bị ảnh hưởng, đây là dạng nghiêm trọng nhất. Các dấu hiệu và triệu chứng của bệnh thalassemia thể nặng xuất hiện trong hai năm đầu đời, đầu tiên là thiếu máu trầm trọng, phát triển bất thường, xanh xao hoặc vàng da và vàng mắt, khó chịu và nhiễm trùng thường xuyên. Trẻ bị ảnh hưởng đến sự phát triển lá lách, gan và tim lớn hơn bình thường. Trẻ cũng có thể phát triển các dị tật về xương. Tình trạng thiếu máu ở những bệnh nhi này có thể nghiêm trọng đến mức trẻ phải truyền máu thường xuyên.
Việc điều trị có thể khác nhau tùy thuộc vào biểu hiện lâm sàng của bệnh và có thể phải truyền máu thường xuyên, thuốc thải sắt có thể được sử dụng để giảm lượng sắt dư thừa do truyền máu nhiều lần, bổ sung axit folic và cấy ghép tủy xương. Chẩn đoán sớm và điều trị đầy đủ có thể giúp tránh các biến chứng và cải thiện chất lượng cuộc sống của những người bị ảnh hưởng.

Lời khuyên từ chúng tôi
Bạn có nguy cơ thấp mắc bệnh, tuy nhiên bạn phải luôn theo dõi, khi có bất kỳ biểu hiện bất thường đã được nêu ở trên, hãy liên hệ với bác sĩ để được chẩn đoán và tư vấn về dinh dưỡng, lối sống, điều trị.
Bạn nên có một chế độ dinh dưỡng hợp lý để phát triển tốt nhất. Luôn theo dõi, khi có triệu chứng bất thường trong quá trình phát triển, hãy liên hệ với bác sĩ để được chẩn đoán và tư vấn. Không tự ý bắt đầu bất kỳ điều trị nào mà chưa hỏi ý kiến của bác sĩ.
'''
    print(get_detail(src))
