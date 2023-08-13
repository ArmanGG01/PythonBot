<?php
// Token bot Anda dari BotFather
define('BOT_TOKEN', '6315172994:AAE-nSTwK6xgewRkiybt2YGPvZ8kBZDzbrw');

// Fungsi untuk mengirim pesan
function sendMessage($chatID, $message, $replyMarkup = null) {
    $url = 'https://api.telegram.org/bot' . BOT_TOKEN . '/sendMessage';
    $data = array('chat_id' => $chatID, 'text' => $message, 'reply_markup' => $replyMarkup);
    $options = array(
        'http' => array(
            'method'  => 'POST',
            'content' => http_build_query($data),
            'header'  => "Content-Type: application/x-www-form-urlencoded\r\n"
        )
    );
    $context  = stream_context_create($options);
    file_get_contents($url, false, $context);
}

// Mendapatkan input dari pengguna
$update = json_decode(file_get_contents("php://input"), TRUE);
$chatID = $update['message']['chat']['id'];
$message = $update['message']['text'];

// Daftar respon acak
$responses = array(
    "Halo! Bagaimana kabarmu?",
    "Apa kabar?",
    "Sedang apa?",
    "Punya rencana apa hari ini?",
    "Hobi kamu apa?",
    "Aku suka berbicara tentang cuaca.",
    "Ada yang menarik yang terjadi baru-baru ini?"
);

// Tombol inline
$inlineKeyboard = json_encode(array(
    'inline_keyboard' => array(
        array(
            array('text' => 'Halo', 'callback_data' => 'halo'),
            array('text' => 'Apa kabar?', 'callback_data' => 'apa_kabar')
        )
    )
));

// Menentukan respon
if (strtolower($message) == "/start") {
    $response = "Halo! Aku adalah bot gabut. Apa yang ingin kamu tanyakan?";
} elseif (strtolower($message) == "/options") {
    sendMessage($chatID, "Pilih opsi:", $inlineKeyboard);
    exit;
} else {
    $response = $responses[array_rand($responses)];
}

// Mengirim respon
sendMessage($chatID, $response);
?>
