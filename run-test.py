
import streamlit as st
from shorten import shorten
from detail import get_detail
from genz import genZ_transfer


ip1 = """Kết quả của bạn: Đáp ứng thuận lợi
Hướng dẫn sử dụng thuốc: Đối với PEG-INF alpha và RBV: Khoảng 70% cơ hội có đáp ứng virus kéo dài sau 48 tuần điều trị. Cân nhắc các hệ quả trước khi bắt đầu phác đồ chứa PEG-IFN alpha và RBV. Đối với sự kết hợp Thuốc ức chế Protease với PEG-INF alpha và RBV: khoảng 90% cơ hội có đáp ứng virus kéo dài sau 24-48 tuần điều trị. Khoảng 80-90% bệnh nhân đủ điều kiện để điều trị rút ngắn (24-28 tuần so với 48 tuần). Cân nhắc ủng hộ việc sử dụng phác đồ có chứa PEG-IFN alpha và RBV.
Ý nghĩa: Khoảng 70% cơ hội có đáp ứng virus kéo dài sau 48 tuần điều trị. Cân nhắc các hệ quả trước khi bắt đầu phác đồ chứa PEG-IFN alpha và RBV.
"""

ip2 = """Bạn có khuynh hướng cử động chân tay liên tục khi nghỉ ngơi. Kiểu gen của bạn liên quan đến hội chứng này tăng nhẹ trên trung bình.
1/ Nền tảng khoa học
Hầu hết chúng ta đều ít nhiều cử động một số bộ phận trên cơ thể trong vô thức, khi bắt đầu ngủ và trong giấc ngủ. Tuy nhiên, một số người khác lại có cảm giác khó chịu ở tay chân (thấy ngứa, châm chích), không thể cưỡng lại nên phải cử động tay chân liên tục trong khi nghỉ ngơi để giảm cảm giác này. Đôi khi, đây cũng có thể là một dấu hiệu của rối loạn thần kinh gọi là hội chứng Chân không nghỉ (restless leg syndrome - RLS), xảy ra ở mọi độ tuổi. Đây có thể là nguyên nhân chính gây ra gián đoạn giấc ngủ. Hội chứng Chân không nghỉ khá phổ biến, chiếm khoảng 15% người, tùy thuộc vào nhóm dân số nghiên cứu. Nguyên nhân của hội chứng này chưa được hiểu rõ, nhưng một số khác biệt về gen, cũng như nồng độ sắt trong máu đã được ghi nhận là có liên quan. Một số khác biệt được ghi nhận trên gen BTBD9 có liên quan đến hội chứng Chân không nghỉ. Mặc dù chức năng chính xác của gen này và cách nó ảnh hưởng đến giấc ngủ hiện vẫn chưa được làm rõ. Tuy nhiên, nghiên cứu trên chuột và ruồi với gen BTBD9 bị biến đổi đã chứng minh là có liên quan đến rối loạn giấc ngủ.
2/ Kiểu gen của bạn
Kiểu gen của bạn có liên quan đến tình trạng tăng nhẹ nguy cơ phát triển các cử động chân định kỳ khi ngủ và/hoặc RLS.
3/ Khuyến nghị
Mục tiêu điều trị hội chứng Chân không nghỉ là kiểm soát tình trạng, giảm các triệu chứng và cải thiện giấc ngủ.
Ở mức độ nhẹ đến trung bình, người bệnh cần thay đổi lối sống:
Đảm bảo khẩu phần ăn cung cấp đủ chất sắt
Bắt đầu chương trình thể dục đều đặn (như đi bộ) với cường độ vừa phải
Thiết lập giấc ngủ khoa học, hạn chế tiếng ồn
Hạn chế caffeine, rượu bia; tránh xa thuốc lá
Xoa bóp chân nhẹ nhàng, tắm nước ấm, dùng đệm sưởi hoặc túi nước đá áp dụng cho chân
Giảm căng thẳng, giữ tinh thần thoải mái
Tuy nhiên, cần đến khám ở các cơ sở y tế chuyên nghiệp để được bác sĩ kiểm tra và theo dõi.
Các yếu tố khác có thể liên quan đến hội chứng Chân không nghỉ:
Tuổi tác: Càng lớn tuổi càng có khuynh hướng xuất hiện hội chứng này.
Di truyền: Tiền sử gia đình.
Giới tính: Phụ nữ thường được chẩn đoán mắc RLS hơn nam giới. Một số phụ nữ đang mang thai có thể xuất hiện hội chứng này nhưng hầu hết tự khỏi sau sinh.
Do các bệnh lý khác: chẳng hạn thiếu sắt, bệnh thận giai đoạn cuối, tổn thương thần kinh.
Do dùng một số thuốc.
LƯU Ý
Phân tích này không khảo sát tất cả biến thể liên quan đến hội chứng Chân không nghỉ; không thay thế xét nghiệm chẩn đoán. Nguy cơ phát triển hội chứng này còn tùy thuộc vào các yếu tố khác như tuổi tác, tiền sử gia đình.
Nếu bạn lo lắng nguy cơ của mình, hãy tham vấn bác sĩ và tuân thủ phác đồ điều trị từ chuyên gia y tế.
"""


ip3 = """Nền tảng khoa học
Suy giáp bẩm sinh (CH) là một bệnh đặc trưng bởi sự thiếu hụt hoàn toàn hoặc một phần hormone tuyến giáp ngay từ khi sinh ra, do những bất thường về chức năng và cấu trúc của tuyến giáp. CH là bệnh nội tiết phổ biến nhất trên toàn thế giới. Mặc dù hầu hết các trường hợp CH là lẻ tẻ (không có tiền sử gia đình), có một tỷ lệ phần trăm có di truyền lặn trên NST thường. Nói chung, không có dấu hiệu hoặc triệu chứng nào xuất hiện khi sinh, mặc dù một số trẻ có thể ít hoạt động hơn và ngủ nhiều hơn bình thường.
Nếu không được điều trị kịp thời, các triệu chứng khác sẽ xuất hiện như trương lực cơ thấp, lưỡi to, thoát vị rốn, nhịp tim thấp và da và mắt có sắc tố vàng xanh kéo dài hơn hai tuần sau khi sinh. Tiên lượng về thần kinh phụ thuộc vào việc thiết lập điều trị sớm và thành công, dựa trên việc sử dụng các hormone tuyến giáp và theo dõi y tế. Nếu không được điều trị, trẻ em bị ảnh hưởng có thể bị khuyết tật trí tuệ, chậm phát triển và các biến chứng toàn thân. Nếu điều trị được bắt đầu trong hai tuần đầu tiên sau khi sinh, trẻ sơ sinh có thể phát triển bình thường.

Lời khuyên từ chúng tôi
Bạn có nguy cơ thấp mắc bệnh, tuy nhiên bạn phải luôn theo dõi, khi có bất kỳ biểu hiện bất thường đã được nêu ở trên, hãy liên hệ với bác sĩ để được chẩn đoán và tư vấn về dinh dưỡng, lối sống, điều trị.
Bạn nên có một chế độ dinh dưỡng hợp lý để phát triển tốt nhất. Luôn theo dõi, khi có triệu chứng bất thường trong quá trình phát triển, hãy liên hệ với bác sĩ để được chẩn đoán và tư vấn. Không tự ý bắt đầu bất kỳ điều trị nào mà chưa hỏi ý kiến của bác sĩ.
"""


ip4 = """Cơ sở khoa học
Da mi chảy xệ là tình trạng vùng da quanh mắt bị thừa, chùng nhão, kém đàn hồi khiến da mí mắt nhăn nheo, rũ xuống, làm mất nếp 2 mí và mắt nhỏ lại. Hiện nay, nhiều phụ nữ thường tìm đến phương pháp thẩm mỹ cắt bớt vùng da mi mắt, căng chỉ collagen... để da mi căng trẻ, đàn hồi trở lại. Tuy nhiên, để ngăn ngừa hiện tượng này, cần hiểu rõ cơ chế xuất hiện và cơ địa da của mỗi người để chăm sóc kịp thời.

Cơ chế da mi chảy xệ:
Theo thời gian, da sẽ mất đi hai loại protein quan trọng được sản xuất trong lớp hạ bì là elastin và collagen. Trong đó, elastin mang lại độ đàn hồi cho da, giúp làn da săn chắc. Collagen được sản xuất bởi các nguyên bào sợi, có cấu trúc chặt chẽ, giúp da duy trì độ săn chắc. Cả hai protein này sẽ dần suy giảm hoặc mất dần theo tuổi tác; tuy nhiên, mi mắt nói riêng và vùng da quanh mắt (bao gồm bọng mắt, đuôi mắt) nói chung sẽ chịu tác động đầu tiên, do mô da mỏng so với các phần khác trên cơ thể.
Ngoài ra, cần chú ý các yếu tố bên ngoài ảnh hưởng đến làn da quanh mắt như:
Tiếp xúc với tia cực tím
Chất ô nhiễm trong môi trường như khói thuốc lá
Lối sống: Thức khuya, nheo mắt do hoạt động lâu dưới trời nắng, thói quen biểu cảm...
Chế độ dinh dưỡng kém, không hỗ trợ tăng sinh collagen và elastin
Chu trình chăm sóc da không đảm bảo

Kết quả của bạn
Tuyệt vời! Kiểu gen của bạn có khuynh hướng "bảo vệ" cơ mí mắt khỏi lão hóa.
Biến thể gen này có liên quan đến khả năng ngăn ngừa tốt tình trạng sụp mí mắt.
"""


ip5 = """Kết quả điển hình
Khuynh hướng phát triển lòng tự tin ở mức cân bằng.

Giới thiệu
Tự tin là cách chúng ta tin tưởng, nhìn nhận các giá trị, năng lực của bản thân. Nó bao gồm niềm tin về năng lực, đánh giá về ngoại hình, thái độ hoặc hành vi mà chúng ta dành cho cơ thể của mình. Lòng tự tin đóng vai trò quan trọng để tạo ra động lực và thành công.
Sự tự tin lành mạnh có thể dẫn dắt chúng ta có cái nhìn tích cực để hoàn thành các mục tiêu trong cuộc sống. Ngược lại, việc kém tự tin có thể cản trở năng lực của một người. Lòng tự tin, cũng như các đặc điểm tính cách khác, một phần chịu ảnh hưởng bởi các biến thể di truyền khác nhau ở mỗi người.
"""

n_short_sentences = 3
n_genz_sentences = 4
input_text = ip1

print('short style')
print(shorten(input_text, n_short_sentences))
print('-'*100)


print('GenZ style')
short = shorten(input_text, n_genz_sentences)
print(genZ_transfer(short))
print('-'*100)


detail_text = input_text
for key, value in get_detail(input_text).items():
        if value != '':
            detail_text += '\n' + '-'*100 + '\n' + key + ': ' + value
print('Analytic style:')
print(detail_text)

