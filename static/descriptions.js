/* static/descriptions.js */

const KEIRSEY_DESCRIPTIONS = {
    "Artisan": {
        "title": "The Artisan (SP)",
        "desc": "Anda berorientasi pada tindakan, adaptif, dan menyukai kebebasan. Anda unggul dalam situasi yang membutuhkan taktik dan penanganan masalah secara langsung.",
        "roles": ["Promoter", "Crafter", "Performer", "Composer"] 
    },
    "Guardian": {
        "title": "The Guardian (SJ)",
        "desc": "Anda menghargai stabilitas, aturan, dan tradisi. Anda dapat diandalkan, detail, dan bekerja keras untuk menjaga ketertiban dalam organisasi atau keluarga.",
        "roles": ["Supervisor", "Inspector", "Provider", "Protector"]
    },
    "Idealist": {
        "title": "The Idealist (NF)",
        "desc": "Anda berfokus pada pertumbuhan pribadi, empati, dan makna hidup. Anda antusias, intuitif, dan sangat peduli pada hubungan antarmanusia.",
        "roles": ["Teacher", "Counselor", "Champion", "Healer"]
    },
    "Rational": {
        "title": "The Rational (NT)",
        "desc": "Anda berorientasi pada logika, kompetensi, dan pemahaman sistem. Anda skeptis, strategis, dan selalu mencari cara untuk meningkatkan efisiensi.",
        "roles": ["Fieldmarshal", "Mastermind", "Inventor", "Architect"]
    }
};

const MBTI_DETAILS = {
    "ESTP": { "role": "Promoter", "desc": "Energik, penuh gaya, dan pragmatis. Suka mengambil risiko dan memecahkan masalah segera." },
    "ISTP": { "role": "Crafter", "desc": "Tenang namun impulsif. Ahli menggunakan alat dan sangat mandiri." },
    "ESFP": { "role": "Performer", "desc": "Ramah, spontan, dan suka menghibur orang lain. Hidup untuk saat ini." },
    "ISFP": { "role": "Composer", "desc": "Seniman yang tenang, sensitif, dan baik hati. Menghindari konflik dan menghargai estetika." },
    "ESTJ": { "role": "Supervisor", "desc": "Administrator yang tegas dan efisien. Suka mengatur orang dan proyek." },
    "ISTJ": { "role": "Inspector", "desc": "Bertanggung jawab, serius, dan sangat tertib. Menjunjung tinggi fakta dan tradisi." },
    "ESFJ": { "role": "Provider", "desc": "Sangat peduli, populer, dan suka melayani orang lain. Mengutamakan harmoni sosial." },
    "ISFJ": { "role": "Protector", "desc": "Pelindung yang setia, hangat, dan teliti. Selalu siap membela orang yang dicintai." },
    "ENFJ": { "role": "Teacher", "desc": "Pemimpin yang karismatik dan inspiratif. Mampu melihat potensi dalam diri orang lain." },
    "INFJ": { "role": "Counselor", "desc": "Pencari makna yang mendalam, visioner, dan idealis. Mengerti orang lain dengan sangat baik." },
    "ENFP": { "role": "Champion", "desc": "Antusias, kreatif, dan bebas. Selalu melihat kemungkinan baru dalam hidup." },
    "INFP": { "role": "Healer", "desc": "Puitis, baik hati, dan altruistik. Selalu ingin membantu tujuan yang baik." },
    "ENTJ": { "role": "Fieldmarshal", "desc": "Pemimpin strategis yang tegas. Mampu mengorganisir perubahan besar." },
    "INTJ": { "role": "Mastermind", "desc": "Pemikir imajinatif dan strategis. Memiliki rencana untuk segala hal." },
    "ENTP": { "role": "Inventor", "desc": "Pemikir cerdas yang suka tantangan intelektual dan berdebat." },
    "INTP": { "role": "Architect", "desc": "Penemu yang inovatif dengan haus akan pengetahuan yang tak terpuaskan." }
};

// PERBAIKAN DI SINI: Menghapus
const DIMENSION_EXPLANATIONS = {
    "E": "Anda cenderung **Expressive (E)**. Anda mendapatkan energi dari interaksi sosial dan aktivitas luar.",
    "I": "Anda cenderung **Reserved (I)**. Anda lebih nyaman dengan ketenangan dan memproses pikiran secara internal.",
    "S": "Anda bersifat **Observant (S)**. Anda fokus pada fakta nyata, pengalaman konkret, dan apa yang terjadi saat ini.",
    "N": "Anda bersifat **Introspective (N)**. Anda lebih tertarik pada ide, teori, masa depan, dan kemungkinan abstrak.",
    "T": "Anda adalah **Tough-minded (T)**. Anda mengambil keputusan berdasarkan logika objektif dan analisis sebab-akibat.",
    "F": "Anda adalah **Friendly (F)**. Anda mengambil keputusan berdasarkan nilai-nilai pribadi dan dampaknya pada orang lain.",
    "J": "Anda memiliki gaya **Scheduling (J)**. Anda suka rencana yang teratur, keputusan yang pasti, dan keteraturan.",
    "P": "Anda memiliki gaya **Probing (P)**. Anda fleksibel, spontan, dan suka membiarkan opsi tetap terbuka."
};