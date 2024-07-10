import json
import re
import PyPDF2
import openai

openai.api_key = 'OPEN_AI_KEY'

def pdf_to_text(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def clean_text(text):
    #Veri Manipülasyon yapısı
    text = re.sub(r'\d+\.\s+', '', text)  #Madde Numaralarını Temizlemek için kullandım
    text = re.sub(r'\n+', ' ', text)  #Gereksiz yeni satırları temizlemek için kullandım
    text = re.sub(r'\s{2,}', ' ', text)  #Gereksiz boşlukları temizlemek için kullandım
    text = re.sub(r'[^\S\r\n]+', ' ', text)  #Gereksiz boşlukları boş satır bazında silmek için kullandım
    text = re.sub(r'(MADDE \d+|BÖLÜM \d+)', '', text)  #Context olarak madde ve bölüm yazan yapıları almamak için kullandım
    return text.strip()

def split_text_into_sentences(text):
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text) #Metni cümlelere bölmek için context yapıları cümle ortasından başlamasını engellemek için kullandım
    return sentences

def get_context_chunks(sentences, max_chunk_size=50):
    #Ouşturulacak json yapılarını ortalama 50 kelime olması için chun_size yapılarını oluşturdum.
    chunks = []
    current_chunk = []

    for sentence in sentences:
        current_chunk.append(sentence)
        if len(' '.join(current_chunk).split()) >= max_chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []

    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks

def analyze_text_with_gpt(text):
    #prompt yapısını tam anlamıyla anlaması için ekstra ekstra açıklayıcı ve örnekleyici bir yolla ilerledim.
    example_json2 = {
        "context": "Kooperatiflerin kurumlar vergisi muafiyetinden yararlanabilmeleri için ana sözleşmelerinde; Sermaye üzerinden kazanç dağıtılmamasına, Yönetim kurulu başkan ve üyelerine kazanç üzerinden pay verilmemesine, Yedek akçelerinin ortaklara dağıtılmamasına, Sadece ortaklarla iş görülmesine dair hükümlerin bulunması ve bu kayıt ve şartlara da fiilen uyulması gerekmektedir.",
        "question": "Kooperatiflerin kurumlar vergisi muafiyetinden yararlanabilmesi için ana sözleşmelerinde hangi hükümlerin bulunması gerekmektedir?",
        "answer": "Sermaye üzerinden kazanç dağıtılmaması, yönetim kurulu başkan ve üyelerine kazanç üzerinden pay verilmemesi, yedek akçelerin ortaklara dağıtılmaması ve sadece ortaklarla iş görülmesine dair hükümlerin bulunması gerekmektedir. (Madde 4, Fıkra 1, Bent k)"
    }

    example_json3 = {
        "context": "20/5/2006 tarih ve 26173 sayılı Resmi Gazete’de yayımlanarak aynı tarihte yürürlüğe giren 5502 sayılı Sosyal Güvenlik Kurumu Kanununun geçici 1 inci maddesine göre, T.C. Emekli Sandığı, Bağ-Kur ve Sosyal Sigortalar Kurumu, Kanunun yürürlük tarihi itibarıyla Sosyal Güvenlik Kurumuna devredildiğinden, anılan Kanuna göre kurulan Sosyal Güvenlik Kurumu da kurumlar vergisinden muaf olacaktır.",
        "question": "5502 sayılı Sosyal Güvenlik Kurumu Kanunu'na göre hangi kurumlar kurumlar vergisinden muaftır?",
        "answer": "T.C. Emekli Sandığı, Bağ-Kur ve Sosyal Sigortalar Kurumu, 5502 sayılı Sosyal Güvenlik Kurumu Kanunu'nun yürürlük tarihi itibarıyla Sosyal Güvenlik Kurumuna devredildiğinden, Sosyal Güvenlik Kurumu kurumlar vergisinden muaftır. (Madde 4, Fıkra 1, Bent e)"
    }

    prompt = (
        "Amacım bir LLM modeli eğitmek. Bunun için, bana sağlanan metinden JSON formatında belirli bilgileri çıkartmanı istiyorum. "
        "'context', 'question' ve 'answer' içermelidir. 'context' tam ve anlamlı cümlelerden oluşmalıdır ve soru işareti içermemelidir. "
        "'question' context'e dayanarak oluşturulmalı ve 'answer' context'teki bilgilerden yararlanarak mantıklı bir yanıt içermelidir. "
        "Her cevap context ile aynı cümleleri içermemelidir. Çıktıların JSON formatında şu şekilde olmasını istiyorum:\n"
        "{\n"
        "    \"context\": \"<PDF'den alıntı>\",\n"
        "    \"question\": \"<context'e dayalı soru>\",\n"
        "    \"answer\": \"<soruya verilen mantıklı cevap>\"\n"
        "}\n"
        "Örnek:\n"
        f"{json.dumps(example_json2, ensure_ascii=False, indent=4)}\n"
        f"{json.dumps(example_json3, ensure_ascii=False, indent=3)}\n"
        "Aşağıdaki metni kullanarak JSON formatında benzer yapıda çıktılar oluştur:\n"
        f"Metin: {text}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are the best pdf analyser and problem solver assistant."}, #Onu motive ettim....
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000, #Token olarak 2000 seçtim chatgpt-3.5 turbo modeli max 4096 destekliyor. Bu yüzden 2000 gayet yeterli oldu deneme yanılma yoluyla belirledim.
        temperature=0.5, #Yaratıcılığı da deneme yanılma yollarıyla analiz ettikten sonra ilgili proje için en uygununun 0.5 olduğu kararına vardım.
    )

    result_text = response['choices'][0]['message']['content'] #responsların gelip gelmediğini kontrol edebilmek açısından basit bir karar kontrol yapısı oluşturdum.
    if not result_text:
        print("API returned an empty response.")
    return result_text

def process_pdf_files(pdf_paths):
    #json encode işlemleri ve bunların yanında json formatına bölebilmek için veri manipülasyonlarını process_pdf_files fonksiyonunda belirttim.
    all_qa_pairs = []

    for pdf_path in pdf_paths:
        #Genel anlamıyla manipülasyonlarıma devam ettim.
        print(f"Processing {pdf_path}...")
        text = pdf_to_text(pdf_path) #ilgili path dosyalarından gelen dokümanları texte çevirmek için yukarıda tanımladığım pdf_to_text fonksiyonunu çağırıp path dosyamı içerisine aktardım.
        cleaned_text = clean_text(text)
        sentences = split_text_into_sentences(cleaned_text)
        chunks = get_context_chunks(sentences, max_chunk_size=50)
        
        for chunk in chunks:
            result_text = analyze_text_with_gpt(chunk)
            json_objects = result_text.strip().split('\n}\n{')
            json_objects = ['{' + obj + '}' if not obj.startswith('{') else obj for obj in json_objects]
            json_objects = [obj + '}' if not obj.endswith('}') else obj for obj in json_objects]
            
            for obj in json_objects:
                #basit bir try expect yapısı kurdum çünkü sistem json encode yapılarında problem çektiğinde işleme devam etmesini istedim.
                try:
                    data = json.loads(obj)
                    print("Successfully parsed JSON data:", data)
                    all_qa_pairs.append(data)
                except json.JSONDecodeError as e:
                    print("JSON decode error:", e)
                    print("Received text:", obj)

    return {
        "soru_cevap": all_qa_pairs #json formatında olan verileri soru_cevap anahtarı içerisinde tuttum.
    }

def save_data_to_json(data, json_path):
    #klasik bir şekilde json dosyamı kaydetmek üzere basit bir fonksiyon oluşturdum.
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4) #indent parametresini 4 seçtim genel olarak 5, 4 veya 3 seçerim. Bu değerlerin json formatındaki verileri daha okunabilir ve göz zevkime uygun olduğunu düşünüyorum.
    print(f"Data successfully saved to {json_path}")

pdf_paths = [
    ""
]

combined_data = process_pdf_files(pdf_paths) #alınan path'e göre işlemi başlatıyorum.
save_data_to_json(combined_data, "veri_seti.json") #en sonunda artık işlem tamamlanıyor ve oluşan json yapımı sistemime kaydediyorum.
print("Processing complete.")