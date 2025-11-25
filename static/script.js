/* static/script.js */

// --- Variabel Global ---
let quizData = [];              // Menampung data soal dari Python Backend
let currentQuestionIndex = 0;   // Melacak nomor soal saat ini (dimulai dari 0)

// Object untuk menyimpan akumulasi skor Fuzzy Logic
// Struktur ini harus cocok dengan output dari file engine/model.py teman Anda
let fuzzyScores = {
    // 8 Traits MBTI
    E: 0.0, I: 0.0, 
    S: 0.0, N: 0.0, 
    T: 0.0, F: 0.0, 
    J: 0.0, P: 0.0,
    // 4 Traits Keirsey
    A: 0.0,      // Artisan
    G: 0.0,      // Guardian
    I_temp: 0.0, // Idealist (menggunakan I_temp agar beda dengan I Introvert)
    R: 0.0       // Rational
};

// --- Referensi Elemen DOM (HTML) ---
const startScreen = document.getElementById('start-screen');
const quizScreen = document.getElementById('quiz-screen');
const resultScreen = document.createElement('div'); // Kita buat dinamis nanti atau bisa tambah di HTML

const startButton = document.getElementById('start-button');
const questionText = document.getElementById('question-text');

// Tombol Jawaban
const btnOptionA = document.getElementById('option-a-button');
const btnOptionB = document.getElementById('option-b-button');
const textOptionA = document.getElementById('option-a-text');
const textOptionB = document.getElementById('option-b-text');

// Elemen Display Skor
const scoreArtisan = document.getElementById('score-artisan');
const scoreGuardian = document.getElementById('score-guardian');
const scoreIdealist = document.getElementById('score-idealist');
const scoreRational = document.getElementById('score-rational');

const mbtiEI = document.getElementById('mbti-e-i');
const mbtiSN = document.getElementById('mbti-s-n');
const mbtiTF = document.getElementById('mbti-t-f');
const mbtiJP = document.getElementById('mbti-j-p');

// --- 1. Fungsi Mengambil Data dari Backend (Flask) ---
async function fetchQuizData() {
    try {
        console.log("Mengambil data dari server...");
        // Memanggil API yang kita buat di app.py
        const response = await fetch('/api/get-quiz-data');
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
            alert("Terjadi kesalahan di server: " + data.error);
            return;
        }

        quizData = data;
        console.log(`Berhasil memuat ${quizData.length} pertanyaan.`);

        // Aktifkan tombol start setelah data siap
        startButton.disabled = false;
        startButton.innerText = "START";
        startButton.style.cursor = "pointer";

    } catch (error) {
        console.error("Gagal mengambil data:", error);
        questionText.innerText = "Gagal memuat soal. Pastikan file 'app.py' sedang berjalan.";
        startButton.innerText = "Error Loading";
    }
}

// --- 2. Logika Memulai & Navigasi Kuis ---

function startQuiz() {
    if (quizData.length === 0) {
        alert("Data soal belum siap!");
        return;
    }
    
    // Reset Skor dan Index
    currentQuestionIndex = 0;
    resetScores();
    updateScoreDisplay(); // Reset tampilan ke 0

    // Ganti Layar
    startScreen.classList.add('hidden');
    quizScreen.classList.remove('hidden');
    
    // Muat soal pertama
    loadQuestion(currentQuestionIndex);
}

function loadQuestion(index) {
    // Ambil data soal berdasarkan index array
    const q = quizData[index];
    
    // Animasi sederhana (fade in effect)
    questionText.style.opacity = 0;
    setTimeout(() => {
        questionText.innerText = q.text; // Teks Soal
        textOptionA.innerText = q.a;     // Teks Opsi A
        textOptionB.innerText = q.b;     // Teks Opsi B
        questionText.style.opacity = 1;
    }, 200);
}

// --- 3. Logika Pemrosesan Jawaban ---

function processAnswer(choice) {
    const q = quizData[currentQuestionIndex];
    let selectedScores = {};

    // Tentukan bobot skor mana yang diambil (A atau B)
    // Data 'scoresA' dan 'scoresB' dikirim dari app.py
    if (choice === 'A') {
        selectedScores = q.scoresA;
    } else {
        selectedScores = q.scoresB;
    }

    // Tambahkan bobot ke skor global (Fuzzy Accumulation)
    for (let key in selectedScores) {
        // Pastikan key ada di objek fuzzyScores kita (untuk keamanan)
        if (fuzzyScores.hasOwnProperty(key)) {
            // Konversi ke float untuk memastikan penjumlahan angka
            fuzzyScores[key] += parseFloat(selectedScores[key]);
        }
    }

    // Perbarui tampilan skor di Header
    updateScoreDisplay();

    // Lanjut ke soal berikutnya
    currentQuestionIndex++;

    if (currentQuestionIndex < quizData.length) {
        loadQuestion(currentQuestionIndex);
    } else {
        finishQuiz();
    }
}

// --- 4. Update Tampilan Skor (Bagian Paling Menarik) ---

function updateScoreDisplay() {
    // Update Skor Keirsey (tampilkan 2 angka di belakang koma)
    scoreArtisan.innerText = fuzzyScores.A.toFixed(2);
    scoreGuardian.innerText = fuzzyScores.G.toFixed(2);
    scoreIdealist.innerText = fuzzyScores.I_temp.toFixed(2);
    scoreRational.innerText = fuzzyScores.R.toFixed(2);

    // Update MBTI Dominance (Logika: Tampilkan huruf yang skornya lebih besar)
    
    // E vs I
    mbtiEI.innerText = (fuzzyScores.E >= fuzzyScores.I) ? "E" : "I";
    mbtiEI.style.color = (fuzzyScores.E >= fuzzyScores.I) ? "#FFD700" : "#fff"; // Highlight Emas

    // S vs N
    mbtiSN.innerText = (fuzzyScores.S >= fuzzyScores.N) ? "S" : "N";
    
    // T vs F
    mbtiTF.innerText = (fuzzyScores.T >= fuzzyScores.F) ? "T" : "F";
    
    // J vs P
    mbtiJP.innerText = (fuzzyScores.J >= fuzzyScores.P) ? "J" : "P";
}

function resetScores() {
    for (let key in fuzzyScores) {
        fuzzyScores[key] = 0.0;
    }
}

// --- 5. Menyelesaikan Kuis ---

function finishQuiz() {
    quizScreen.classList.add('hidden');
    
    // Hitung Hasil Akhir
    const finalMBTI = 
        ((fuzzyScores.E >= fuzzyScores.I) ? "E" : "I") +
        ((fuzzyScores.S >= fuzzyScores.N) ? "S" : "N") +
        ((fuzzyScores.T >= fuzzyScores.F) ? "T" : "F") +
        ((fuzzyScores.J >= fuzzyScores.P) ? "J" : "P");

    // Cari Temperamen Keirsey Tertinggi
    const keirseyMap = {
        "Artisan": fuzzyScores.A,
        "Guardian": fuzzyScores.G,
        "Idealist": fuzzyScores.I_temp,
        "Rational": fuzzyScores.R
    };

    // Fungsi mencari key dengan value tertinggi
    let finalKeirsey = Object.keys(keirseyMap).reduce((a, b) => keirseyMap[a] > keirseyMap[b] ? a : b);

    // Tampilkan Layar Hasil (Reuse Start Screen biar simpel, atau buat elemen baru)
    startScreen.classList.remove('hidden');
    startScreen.innerHTML = `
        <h1 style="color: #333;">Hasil Tes Kepribadian</h1>
        
        <div style="background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); margin-bottom: 20px;">
            <p>Tipe MBTI Anda:</p>
            <h2 style="font-size: 3em; color: #00bcd4; margin: 10px 0;">${finalMBTI}</h2>
            
            <p>Temperamen Keirsey:</p>
            <h2 style="font-size: 2em; color: #ff9800; margin: 10px 0;">${finalKeirsey}</h2>
        </div>

        <button id="restart-button" style="
            padding: 15px 30px; 
            font-size: 1.2em; 
            background-color: #333; 
            color: white; 
            border: none; 
            border-radius: 8px; 
            cursor: pointer;">
            Coba Lagi
        </button>
    `;

    // Pasang event listener untuk tombol restart yang baru dibuat
    document.getElementById('restart-button').addEventListener('click', () => {
        window.location.reload(); // Reload halaman untuk reset bersih
    });
}

// --- Event Listeners ---

// Saat halaman selesai dimuat
window.onload = function() {
    // Matikan tombol start dulu sebelum data siap
    startButton.disabled = true;
    startButton.innerText = "Loading Data...";
    
    // Panggil fungsi fetch
    fetchQuizData();
};

// Klik Tombol Start
startButton.addEventListener('click', startQuiz);

// Klik Jawaban A
btnOptionA.addEventListener('click', () => {
    processAnswer('A');
});

// Klik Jawaban B
btnOptionB.addEventListener('click', () => {
    processAnswer('B');
});