# coding=utf-8
import re
import numpy as np
from underthesea import word_tokenize, sent_tokenize
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
    KlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0-9,\.!\?\%\s/()]", " ", out)

    #out = ' '.join(s for s in out.split() if not any(c.isdigit() for c in s))
    out = re.sub(r"[\s]+",' ',out)
    return out.strip()

# RULE BASED:
rule = {
    'luôn' : (0.7, ['lun', 'luông luông', 'lun lun']),
    'luôn luôn' : (0.7, ['lun lun', 'luông luông']),
    'tốt nhất' : (0.9, ['xịn xò nhất']),
    'được' : (0.4, ['đượt']),
    'nhưng mà' : (0.9, ['cơ mà']),
    'tuy nhiên' : (0.8, ['cơ mà']),
    'bị' : (0.4, ['pị']), 
    'phải' : (0.5, ['fải', 'pải']),
    'hợp lý' : (0.7, ['okela']),
    'nhiều' : (0.6, ['nhìu']),
    'tuổi' : (0.6, ['tủi']),
    'hơi' : (0.8, ['hơi pị']),
    'nhé' : (0.9, ['nhứ', 'nhớ', 'nhá', 'nha', ]),
    'như' : (0.75, ['dzư']),
    'thế' : (0.75, ['thí']),
    'tinh thần' : (0.5, ['tâm thần ý lộn tinh thần']),
    'bắt đầu' : (0.5, ['pắt đầu']),

}

rule_pronoun = {
    'tôi' : ['tớ', 'mình', 'tui', 'bần tăng', 'mần', 'tôy'],
    'chúng tôi' : ['chúng tớ', 'chúng mình', 'chúng tui', 'bần tăng', 'chúng mần', 'chúng tôy'],
    'bạn' : ['đồng chí', 'người anh em', 'pạn', 'thí chủ', 'bợn', 'bro'],
    'bác sĩ' : ['bác sĩ','bác sĩ','pác sĩ','đại phu','bác sĩ','bác sĩ' ],
}

intro = ['Về cơ bản là như thí này nhá! ', 'Tóm cái lược lại thì: ', 'Nói như này cho vuông nhứ. ', 'Nói chung là dzư này nè: ',
 'Thui tóm lại thì thế này nhé: ']

advice_suffix = ['nha', 'nhé', 'nhứ', 'nhe']
advice_suffix_prob = 0.8

def changecase(w, islower):
    if islower: return w.lower()
    w = list(w)
    w[0] = w[0].upper()
    w = ''.join(w)
    return w

def detect_advice(ws):
    if ('hãy' in ws) or ('nên' in ws) or ('phải' in ws):
        if 'bạn' in ws:
            return True
    return False

def genZ_transfer(text):
    lines = [clean_text(t) for t in text.split('\n')]
    lines = [t for t in lines if t != '']
    # select a rule pronoun
    idx = np.random.randint(0,len(list(rule_pronoun.values())[0]))
    selected_rule = {w : rule_pronoun[w][idx] for w in rule_pronoun.keys()}
    
    newlines = []
    for line in lines:
        sents = sent_tokenize(line)
        ws = []
        for s in sents: 
            w_in_s = word_tokenize(s)
            if detect_advice(w_in_s) and np.random.rand() < advice_suffix_prob:
                if w_in_s[-1] in ['.',',',':','!','?']:
                    w_in_s.insert(-1, np.random.choice(advice_suffix))
                else:
                    w_in_s.append(np.random.choice(advice_suffix))
            ws.extend(w_in_s)
        ws_new = []
        for w in ws:
            islower = w.islower()
            w = w.lower()
            if w in selected_rule.keys():
                ws_new.append(changecase(selected_rule[w] ,islower))
                continue
            try:
                p, wlist = rule[w]
            except:
                ws_new.append(changecase(w,islower))
                continue
            if np.random.rand() < p:
                ws_new.append(changecase(np.random.choice(wlist), islower))
            else:
                ws_new.append(changecase(w, islower))

        newlines.append(' '.join(ws_new))
    intro_lines = np.random.choice(intro) if 'bro' not in selected_rule.values() else 'Hey bruh, '
    return np.random.choice(intro) + '\n'.join(newlines)
    


if __name__ == '__main__':
    src = '''Kết quả hạn chế
Kiểu gen này cho thấy bạn có khuynh hướng phục hồi hơi khó khăn sau nghịch cảnh. Hãy rèn luyện để tăng cường sức mạnh tinh thần nhé!

Giới thiệu
Sức bật tinh thần (hay khả năng phục hồi) có thể được xem là 'thích ứng tích cực' của con người sau nghịch cảnh. Trên thực tế, các yếu tố gây căng thẳng đến từ cuộc sống hàng ngày có thể phá vỡ trạng thái cân bằng trong tâm lý chúng ta. Tuy nhiên, phục hồi là khả năng xử lý những tình huống bất lợi một cách bình tĩnh và tạo ra kết quả tích cực.
Khả năng phục hồi của các cá nhân khác nhau. Khả năng phục hồi thể hiện sức mạnh thể chất và tinh thần, giúp chúng ta trở lại trạng thái cân bằng sau những tình huống căng thẳng, tạo ra cảm giác vượt lên nghịch cảnh. Khả năng phục hồi có liên quan chặt chẽ với khả năng ổn định về tinh thần và hạnh phúc. Giống như các đặc điểm tinh thần khác, khả năng phục hồi của một người có tương quan với các gen mà họ mang.
'''
    short = shorten(src, 3)
    print(genZ_transfer(short))