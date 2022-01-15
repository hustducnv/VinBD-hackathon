import re
import numpy as np
from underthesea import word_tokenize
from shorten import shorten

def clean_text(text):
    out = re.sub(r'https?:\/\/\S*\s', ' ', text)
    out = re.sub(r"\.\.\.",' ',out)
    out = re.sub(r",",' , ',out)
    out = re.sub(r"\.",' \. ',out)
    out = re.sub(r"!",' ! ',out)
    out = re.sub(r"\?",' \? ',out)
    out = re.sub(r"\%",' \% ',out)
    out = re.sub(r"[^aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJk\
    KlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0-9,\.!\?\%\s]", " ", out)

    #out = ' '.join(s for s in out.split() if not any(c.isdigit() for c in s))
    out = re.sub(r"[\s]+",' ',out)
    return out.strip()

# RULE BASED:
rule = {
    'luôn' : (0.6, ['lun', 'luông luông', 'lun lun']),
    'luôn luôn' : (0.6, ['lun lun', 'luông luông']),
    'tốt nhất' : (0.9, ['xịn xò nhất']),
    'được' : (0.4, ['đượt']),
    'nhưng mà' : (0.9, ['cơ mà']),
    'tuy nhiên' : (0.6, ['cơ mà']),
    'bị' : (0.5, ['pị']), 
    'phải' : (0.3, ['fải']),
}

rule_pronoun = {
    'tôi' : ['tớ', 'mình', 'tui', 'bần tăng', 'tui', 'tôy'],
    'chúng tôi' : ['tớ', 'mình', 'tui', 'bần tăng', 'tui', 'tôy'],
    'bạn' : ['đồng chí', 'người anh em', 'pạn', 'thí chủ', 'bợn', 'bro'],
}

def changecase(w, islower):
    if islower: return w
    w = list(w)
    w[0] = w[0].upper()
    w = ''.join(w)
    return w

def genZ_transfer(text):
    lines = [clean_text(t) for t in text.split('\n')]
    lines = [t for t in lines if t != '']
    # select a rule pronoun
    idx = np.random.randint(0,len(list(rule_pronoun.values())[0]))
    selected_rule = {w : rule_pronoun[w][idx] for w in rule_pronoun.keys()}
    
    newlines = []
    for line in lines:
        ws = word_tokenize(line)
        ws_new = []
        for w in ws:
            islower = w.islower()
            w = w.lower()
            if w in selected_rule.keys():
                ws_new.append(changecase(selected_rule[w],islower))
                continue
            try:
                p, wlist = rule[w]
            except:
                ws_new.append(changecase(w,islower))
                continue
            if np.random.rand() < p:
                ws_new.append(changecase(np.random.choice(wlist), islower))
            else:
                ws_new.append(changecase(w,islower))

        newlines.append(' '.join(ws_new))
    return '\n'.join(newlines)
    


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
    short = shorten(src, 3)
    print(genZ_transfer(short))