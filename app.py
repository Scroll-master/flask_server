from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

# Словарь для отслеживания текущего воспроизводимого файла и процесса
current_media = {
    'process': None,
    'media_url': None
}

@app.route('/api/play', methods=['POST'])
def play_media():
    global current_media
    media_url = request.json.get('media_url')
    
    # Проверка, завершился ли предыдущий процесс
    if current_media['process'] and current_media['process'].poll() is not None:
        current_media['process'] = None  # Обнуляем процесс, если он завершен

    # Если процесс не запущен, начинаем воспроизведение
    if not current_media['process']:
        process = subprocess.Popen(['ffplay', '-autoexit', media_url])
        current_media['process'] = process
        current_media['media_url'] = media_url
        return jsonify({'status': 'playing', 'media_url': media_url})
    else:
        # Если процесс уже запущен, и URL совпадает, игнорируем запрос
        if current_media['media_url'] == media_url:
            return jsonify({'status': 'already playing', 'media_url': media_url})
        # Если URL другой, останавливаем текущий процесс и запускаем новый
        else:
            current_media['process'].terminate()
            process = subprocess.Popen(['ffplay', '-autoexit', media_url])
            current_media['process'] = process
            current_media['media_url'] = media_url
            return jsonify({'status': 'playing new media', 'media_url': media_url})

@app.route('/api/stop', methods=['POST'])
def stop_media():
    global current_media
    if current_media['process']:
        current_media['process'].terminate()
        current_media['process'] = None
        current_media['media_url'] = None
        return jsonify({'status': 'stopped'})
    return jsonify({'status': 'nothing to stop'})


@app.route('/api/status', methods=['GET'])
def get_status():
    # Эта функция должна возвращать текущий статус воспроизведения
    if current_media['process'] and current_media['process'].poll() is None:
        # Процесс все еще запущен
        playing = True
        media_url = current_media['media_url']
    else:
        # Процесс не запущен
        playing = False
        media_url = None
    return jsonify({'playing': playing, 'media_url': media_url})



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
