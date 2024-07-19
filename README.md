        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>PDF to JSON Context-Question-Answer Extraction Tool</h1>

<p>This Python project processes PDF documents to extract meaningful context-question-answer pairs and converts them into a structured JSON format. The primary goal is to assist in training large language models (LLMs) by providing relevant data extracted from PDFs.</p>

<h2>Features</h2>
<ul>
    <li><strong>PDF to Text Conversion:</strong> Uses <code>PyPDF2</code> to read and extract text from PDF documents.</li>
    <li><strong>Text Cleaning:</strong> Cleans extracted text by removing unnecessary elements such as item numbers, excessive whitespace, and irrelevant sections.</li>
    <li><strong>Sentence Splitting:</strong> Splits cleaned text into individual sentences for better processing.</li>
    <li><strong>Context Chunking:</strong> Groups sentences into chunks of approximately 50 words to create meaningful context for questions and answers.</li>
    <li><strong>OpenAI GPT-3.5 Integration:</strong> Utilizes OpenAI's GPT-3.5 model to generate context-question-answer pairs from the text chunks.</li>
    <li><strong>JSON Output:</strong> Formats the generated pairs into a structured JSON file for easy consumption and further processing.</li>
</ul>

<h2>Prerequisites</h2>
<ul>
    <li>Python 3.7+</li>
    <li>Required Python packages:
        <ul>
            <li><code>PyPDF2</code></li>
            <li><code>openai</code></li>
        </ul>
    </li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/ibkya/Automatic-Data-Gainer-System
cd Automatic-Data-Gainer-System</code></pre>
    </li>
    <li>Install the required packages:
        <pre><code>pip install -r requirements.txt</code></pre>
    </li>
    <li>Set up your OpenAI API key:
        <pre><code>openai.api_key = 'your-openai-api-key'</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<ol>
    <li>Place your PDF files in a directory.</li>
    <li>Modify the <code>pdf_paths</code> variable in the script to include the paths to your PDF files.</li>
    <li>Run the script:
        <pre><code>python main.py</code></pre>
    </li>
    <li>The processed data will be saved to <code>veri_seti.json</code>.</li>
</ol>

<h2>Code Explanation</h2>
<ul>
    <li><code>pdf_to_text</code>: Reads and extracts text from a PDF file.</li>
    <li><code>clean_text</code>: Cleans the extracted text by removing unnecessary elements.</li>
    <li><code>split_text_into_sentences</code>: Splits the cleaned text into individual sentences.</li>
    <li><code>get_context_chunks</code>: Groups sentences into chunks of around 50 words.</li>
    <li><code>analyze_text_with_gpt</code>: Uses GPT-3.5 to generate context-question-answer pairs.</li>
    <li><code>process_pdf_files</code>: Orchestrates the entire process for multiple PDF files.</li>
    <li><code>save_data_to_json</code>: Saves the processed data into a JSON file.</li>
</ul>

<h2>Example Output</h2>
<p>The output JSON file will have the following structure:</p>
<pre><code>{
    "soru_cevap": [
        {
            "context": "Kooperatiflerin kurumlar vergisi muafiyetinden yararlanabilmeleri için ana sözleşmelerinde; Sermaye üzerinden kazanç dağıtılmamasına, Yönetim kurulu başkan ve üyelerine kazanç üzerinden pay verilmemesine, Yedek akçelerinin ortaklara dağıtılmamasına, Sadece ortaklarla iş görülmesine dair hükümlerin bulunması ve bu kayıt ve şartlara da fiilen uyulması gerekmektedir.",
            "question": "Kooperatiflerin kurumlar vergisi muafiyetinden yararlanabilmesi için ana sözleşmelerinde hangi hükümlerin bulunması gerekmektedir?",
            "answer": "Sermaye üzerinden kazanç dağıtılmaması, yönetim kurulu başkan ve üyelerine kazanç üzerinden pay verilmemesi, yedek akçelerin ortaklara dağıtılmaması ve sadece ortaklarla iş görülmesine dair hükümlerin bulunması gerekmektedir. (Madde 4, Fıkra 1, Bent k)"
        },
        {
            "context": "20/5/2006 tarih ve 26173 sayılı Resmi Gazete’de yayımlanarak aynı tarihte yürürlüğe giren 5502 sayılı Sosyal Güvenlik Kurumu Kanununun geçici 1 inci maddesine göre, T.C. Emekli Sandığı, Bağ-Kur ve Sosyal Sigortalar Kurumu, Kanunun yürürlük tarihi itibarıyla Sosyal Güvenlik Kurumuna devredildiğinden, anılan Kanuna göre kurulan Sosyal Güvenlik Kurumu da kurumlar vergisinden muaf olacaktır.",
            "question": "5502 sayılı Sosyal Güvenlik Kurumu Kanunu'na göre hangi kurumlar kurumlar vergisinden muaftır?",
            "answer": "T.C. Emekli Sandığı, Bağ-Kur ve Sosyal Sigortalar Kurumu, 5502 sayılı Sosyal Güvenlik Kurumu Kanunu'nun yürürlük tarihi itibarıyla Sosyal Güvenlik Kurumuna devredildiğinden, Sosyal Güvenlik Kurumu kurumlar vergisinden muaf olacaktır. (Madde 4, Fıkra 1, Bent e)"
        }
    ]
}
</code></pre>

<h2>Contributing</h2>
<p>Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <code>LICENSE</code> file for details.</p>

</body>
</html>
