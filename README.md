<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>AI Assistant Projesi README</h1>

<p>Bu proje, kullanıcıların VakıfBank işlemleriyle ilgili sorularına Türkçe dilinde cevap veren bir yapay zeka asistanı oluşturmayı amaçlamaktadır. Kullanıcılar, asistan ile etkileşime geçerek bankacılık işlemleri hakkında bilgi alabilirler. Proje, <code>ollama</code> ve <code>ElevenLabs</code> kütüphanelerini kullanarak kullanıcı girdilerini işleyen ve sesli yanıtlar veren bir sistem geliştirmektedir.</p>

<h2>Özellikler</h2>
<ul>
    <li><strong>Kullanıcı Girdisi İşleme:</strong> Kullanıcıların girdilerini alır ve anlamlı yanıtlar üretir.</li>
    <li><strong>Sesli Yanıt Üretme:</strong> ElevenLabs API'si kullanarak metinleri sesli yanıtlar haline dönüştürür.</li>
    <li><strong>Llama3 Modeli:</strong> Ollama kütüphanesi ile Llama3 modeli kullanarak girdileri işler.</li>
    <li><strong>Türkçe Dil Desteği:</strong> Türkçe dilinde kullanıcı girdilerini anlayıp yanıt verir.</li>
</ul>

<h2>Gereksinimler</h2>
<ul>
    <li>Python 3.7+</li>
    <li>Gerekli Python paketleri:
        <ul>
            <li><code>ollama</code></li>
            <li><code>elevenlabs</code></li>
        </ul>
    </li>
</ul>

<h2>Kurulum</h2>
<ol>
    <li>Depoyu klonlayın:
        <pre><code>git clone https://github.com/your-repo/AI-Assistant
cd AI-Assistant</code></pre>
    </li>
    <li>Gerekli paketleri yükleyin:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>ElevenLabs API anahtarınızı ayarlayın:
        <pre><code>openai.api_key = 'your-elevenlabs-api-key'</code></pre>
    </li>
</ol>

<h2>Kullanım</h2>
<ol>
    <li>Asistanı başlatın ve sorularınızı girin:
        <pre><code>ai_assistant = AI_Assistant()

while True:
    user_input = input("Sorunuzu girin: ")
    if user_input.lower() in ["çıkış", "çık", "quit", "exit"]:
        break
    ai_assistant.handle_input(user_input)</code></pre>
    </li>
    <li>Yanıtlar sesli olarak çalınacaktır.</li>
</ol>

<h2>Kod Açıklaması</h2>
<ul>
    <li><code>AI_Assistant</code>: Kullanıcı girdilerini işlemek ve yanıtları üretmek için ana sınıf.</li>
    <li><code>__init__</code>: ElevenLabs API'sine bağlanır ve başlangıç sistem mesajını ayarlar.</li>
    <li><code>handle_input</code>: Kullanıcı girdisini işleyerek yanıt üretir ve sesli olarak çalar.</li>
</ul>

<h2>Örnek Çıktı</h2>
<p>Yanıtlar ve girdiler tam transcript listesine eklenir ve aşağıdaki yapıda olabilir:</p>
<pre><code>{
    "transcript": [
        {
            "role": "user",
            "content": "Hesap bakiyemi nasıl öğrenebilirim?"
        },
        {
            "role": "assistant",
            "content": "Hesap bakiyenizi öğrenmek için internet bankacılığına giriş yapabilir veya müşteri hizmetlerini arayabilirsiniz."
        }
    ]
}
</code></pre>

<h2>Katkıda Bulunma</h2>
<p>Projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:</p>
<ol>
    <li>Bu depoyu fork'layın.</li>
    <li>Yeni bir dal oluşturun (<code>feature/HarikaOzellik</code>).</li>
    <li>Değişikliklerinizi commit edin (<code>git commit -am 'Harika bir özellik ekledim'</code>).</li>
    <li>Dalınıza push edin (<code>git push origin feature/HarikaOzellik</code>).</li>
    <li>Bir Pull Request oluşturun.</li>
</ol>

<h2>Lisans</h2>
<p>Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.</p>

<h2>İletişim</h2>
<p>Sorularınız veya geri bildirimleriniz için lütfen <a href="mailto:email@example.com">email@example.com</a> adresinden benimle iletişime geçin.</p>

</body>
</html>
