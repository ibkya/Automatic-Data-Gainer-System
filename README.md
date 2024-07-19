<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Assistant Projesi README</title>
</head>
<body>

    <h1>AI Assistant Projesi README</h1>

    <h2>Proje Hakkında</h2>
    <p>Bu proje, kullanıcıların VakıfBank işlemleriyle ilgili sorularına Türkçe dilinde cevap veren bir yapay zeka asistanı oluşturmayı amaçlamaktadır. Kullanıcılar, asistan ile etkileşime geçerek bankacılık işlemleri hakkında bilgi alabilirler. Proje, <code>ollama</code> ve <code>ElevenLabs</code> kütüphanelerini kullanarak kullanıcı girdilerini işleyen ve sesli yanıtlar veren bir sistem geliştirmektedir.</p>

    <h2>Kurulum</h2>

    <h3>Gereksinimler</h3>
    <ul>
        <li>Python 3.7 veya daha üstü</li>
        <li><code>ollama</code> kütüphanesi</li>
        <li><code>ElevenLabs</code> kütüphanesi</li>
    </ul>

    <h3>Adımlar</h3>
    <ol>
        <li>Python ortamınızı oluşturun ve etkinleştirin:
            <pre><code>python -m venv venv
source venv/bin/activate  # Unix
venv\Scripts\activate  # Windows</code></pre>
        </li>
        <li>Gerekli kütüphaneleri yükleyin:
            <pre><code>pip install ollama elevenlabs</code></pre>
        </li>
        <li>ElevenLabs API anahtarınızı alın ve kodda belirtilen yere ekleyin:
            <pre><code>self.client = ElevenLabs(api_key="ELEVEN_LAB_API_KEY")</code></pre>
        </li>
    </ol>

    <h2>Kullanım</h2>

    <h3>Başlatma</h3>
    <p>Asistanı başlatmak için aşağıdaki kodu çalıştırın:</p>
    <pre><code>ai_assistant = AI_Assistant()

while True:
    user_input = input("Sorunuzu girin: ")
    if user_input.lower() in ["çıkış", "çık", "quit", "exit"]:
        break
    ai_assistant.handle_input(user_input)</code></pre>

    <h3>Komutlar</h3>
    <ul>
        <li>Kullanıcı, <code>Sorunuzu girin:</code> promptuna sorusunu yazar ve Enter tuşuna basar.</li>
        <li>Asistan, soruyu işleyerek yanıt verir ve yanıtı sesli olarak çalar.</li>
        <li>Programdan çıkmak için <code>çıkış</code>, <code>çık</code>, <code>quit</code>, veya <code>exit</code> yazmanız yeterlidir.</li>
    </ul>

    <h2>Teknik Detaylar</h2>

    <h3>Yapı</h3>
    <p><strong>AI_Assistant Sınıfı</strong>: Bu sınıf, kullanıcı girdilerini işlemek ve yanıtları üretmek için <code>ollama</code> ve <code>ElevenLabs</code> kütüphanelerini kullanır.</p>
    <ul>
        <li><code>__init__</code> Metodu: ElevenLabs API'sine bağlanır ve başlangıç sistem mesajını ayarlar.</li>
        <li><code>handle_input</code> Metodu: Kullanıcı girdisini işleyerek yanıt üretir ve sesli olarak çalar.</li>
    </ul>

    <h3>Metotlar</h3>
    <p><strong>handle_input(user_input)</strong>:</p>
    <ul>
        <li>Kullanıcı girdisini alır ve <code>ollama</code> kütüphanesi aracılığıyla Llama3 modeline gönderir.</li>
        <li>Alınan yanıtı işleyerek ElevenLabs API'si ile sesli yanıt oluşturur.</li>
        <li>Yanıtı kullanıcıya sesli olarak çalar ve tam transcript listesine ekler.</li>
    </ul>

    <h3>Akış</h3>
    <ol>
        <li>Kullanıcı sorusunu girer.</li>
        <li><code>handle_input</code> metodu bu girdiyi alır.</li>
        <li>Girdi, <code>ollama</code> kütüphanesi aracılığıyla işlenir ve yanıt alınır.</li>
        <li>Yanıt, ElevenLabs API'si ile sesli olarak oluşturulur ve kullanıcıya çalınır.</li>
        <li>Yanıt, tam transcript listesine eklenir.</li>
    </ol>

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
