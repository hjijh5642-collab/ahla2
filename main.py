#!/usr/bin/env python3
"""
فخ ويب دفاعي - تأثيرات مرعبة متطورة
"""
import socket
import threading
import time
from datetime import datetime
import requests
import random

class TerrorWebTrap:
    def __init__(self):
        self.attacks_log = []
        print("💀 فخ الويب المرعب جاهز!")
    
    def log_attack(self, ip, user_agent="غير معروف"):
        """تسجيل هجوم مع معلومات المتصفح"""
        attack_info = {
            'ip': ip,
            'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'user_agent': user_agent,
            'location': self.get_location(ip)
        }
        self.attacks_log.append(attack_info)
        
        print(f"🎣 هجوم مسجل من {ip}")
        print(f"   🌐 المتصفح: {user_agent[:50]}...")
        print(f"   📍 الموقع: {attack_info['location']}")
    
    def get_location(self, ip):
        """الحصول على موقع المهاجم"""
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}', timeout=5)
            data = response.json()
            return f"{data.get('city', 'غير معروف')}, {data.get('country', 'غير معروف')}"
        except:
            return "موقع غير معروف"
    
    def create_web_trap(self, port=8080):
        """إنشاء فخ ويب مع تأثيرات مرعبة"""
        
        def handle_browser_connection(client_socket, client_address):
            """معالجة اتصالات المتصفح"""
            try:
                # استقبال طلب HTTP
                request = client_socket.recv(1024).decode('utf-8')
                lines = request.split('\n')
                
                # استخراج معلومات المتصفح
                user_agent = "غير معروف"
                for line in lines:
                    if 'User-Agent:' in line:
                        user_agent = line.split('User-Agent:')[1].strip()
                        break
                
                # تسجيل الهجوم
                self.log_attack(client_address[0], user_agent)
                
                # إنشاء رد HTTP مرعب
                response = self.create_terror_response(client_address[0])
                
                # إرسال الرد
                client_socket.send(response.encode())
                
            except Exception as e:
                print(f"❌ خطأ في معالجة الاتصال: {e}")
            finally:
                client_socket.close()
        
        # بدء خادم الويب
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('0.0.0.0', port))
        server.listen(5)
        
        print(f"💀 فخ الويب المرعب نشط على: http://localhost:{port}")
        print("🔓 افتح المتصفح وجرب الرابط!")
        print("📝 سيظهر سجل الهجمات هنا عند كل اتصال\n")
        
        while True:
            client, addr = server.accept()
            thread = threading.Thread(target=handle_browser_connection, args=(client, addr))
            thread.start()
    
    def create_terror_response(self, attacker_ip):
        """إنشاء صفحة ويب مرعبة مع تأثيرات متطورة"""
        location = self.get_location(attacker_ip)
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # قائمة الرسائل المخيفة التي ستظهر بعد العداد
        terror_messages = [
            "🚨 SYSTEM BREACH DETECTED 🚨",
            "⚠️ UNAUTHORIZED ACCESS RECORDED ⚠️",
            "🔴 SECURITY PROTOCOL ACTIVATED 🔴",
            "📡 SIGNAL TRACING IN PROGRESS 📡",
            "🌍 GEOLOCATION CONFIRMED 🌍",
            "⚖️ LEGAL ACTION INITIATED ⚖️",
            "🚔 LAW ENFORCEMENT NOTIFIED 🚔",
            "🔒 ALL ACTIVITIES LOGGED 🔒",
            "📊 DIGITAL FOOTPRINT CAPTURED 📊",
            "🛑 CEASE ALL ACTIVITIES NOW 🛑",
            "💀 SYSTEM LOCKDOWN IMMINENT 💀",
            "🔴 CRITICAL SECURITY ALERT 🔴",
            "⚠️ YOUR IDENTITY IS COMPROMISED ⚠️",
            "🚨 POLICE DISPATCHED TO YOUR LOCATION 🚨",
            "🔴 TERMINATE CONNECTION IMMEDIATELY 🔴"
        ]
        
        # بناء HTML مع تأثيرات مرعبة
        html_parts = []
        html_parts.append("HTTP/1.1 200 OK")
        html_parts.append("Content-Type: text/html; charset=utf-8")
        html_parts.append("")
        html_parts.append("<!DOCTYPE html>")
        html_parts.append("<html dir='rtl'>")
        html_parts.append("<head>")
        html_parts.append("    <meta charset='UTF-8'>")
        html_parts.append("    <title>🚨 SYSTEM ALERT</title>")
        html_parts.append("    <style>")
        html_parts.append("        * { margin: 0; padding: 0; box-sizing: border-box; }")
        html_parts.append("        body {")
        html_parts.append("            font-family: 'Courier New', monospace;")
        html_parts.append("            background: #000;")
        html_parts.append("            color: #ff0000;")
        html_parts.append("            overflow: hidden;")
        html_parts.append("            height: 100vh;")
        html_parts.append("        }")
        html_parts.append("        .warning {")
        html_parts.append("            border: 5px solid #ff0000;")
        html_parts.append("            padding: 30px;")
        html_parts.append("            margin: 20px auto;")
        html_parts.append("            max-width: 90%;")
        html_parts.append("            background: #111;")
        html_parts.append("            animation: blink 0.3s infinite;")
        html_parts.append("            text-align: center;")
        html_parts.append("            font-size: 24px;")
        html_parts.append("            font-weight: bold;")
        html_parts.append("        }")
        html_parts.append("        @keyframes blink {")
        html_parts.append("            0%, 50% { border-color: #ff0000; background: #111; }")
        html_parts.append("            51%, 100% { border-color: #000; background: #300; }")
        html_parts.append("        }")
        html_parts.append("        .info {")
        html_parts.append("            background: #222;")
        html_parts.append("            padding: 20px;")
        html_parts.append("            margin: 15px 0;")
        html_parts.append("            border-left: 8px solid #ff0000;")
        html_parts.append("            text-align: right;")
        html_parts.append("            animation: pulse 1s infinite;")
        html_parts.append("        }")
        html_parts.append("        @keyframes pulse {")
        html_parts.append("            0% { opacity: 1; }")
        html_parts.append("            50% { opacity: 0.7; }")
        html_parts.append("            100% { opacity: 1; }")
        html_parts.append("        }")
        html_parts.append("        .countdown {")
        html_parts.append("            font-size: 48px;")
        html_parts.append("            font-weight: bold;")
        html_parts.append("            color: #ff0000;")
        html_parts.append("            margin: 30px 0;")
        html_parts.append("            text-align: center;")
        html_parts.append("            animation: glow 0.5s infinite alternate;")
        html_parts.append("        }")
        html_parts.append("        @keyframes glow {")
        html_parts.append("            from { text-shadow: 0 0 10px #ff0000; }")
        html_parts.append("            to { text-shadow: 0 0 20px #ff0000, 0 0 30px #ff0000; }")
        html_parts.append("        }")
        html_parts.append("        .terror-messages {")
        html_parts.append("            display: none;")
        html_parts.append("            position: fixed;")
        html_parts.append("            top: 0;")
        html_parts.append("            left: 0;")
        html_parts.append("            width: 100%;")
        html_parts.append("            height: 100%;")
        html_parts.append("            background: #000;")
        html_parts.append("            z-index: 1000;")
        html_parts.append("            overflow-y: auto;")
        html_parts.append("        }")
        html_parts.append("        .terror-message {")
        html_parts.append("            font-size: 32px;")
        html_parts.append("            font-weight: bold;")
        html_parts.append("            color: #ff0000;")
        html_parts.append("            text-align: center;")
        html_parts.append("            margin: 20px 0;")
        html_parts.append("            padding: 20px;")
        html_parts.append("            animation: flash 0.2s infinite;")
        html_parts.append("            border: 3px solid #ff0000;")
        html_parts.append("            background: #300;")
        html_parts.append("        }")
        html_parts.append("        @keyframes flash {")
        html_parts.append("            0%, 100% { opacity: 1; transform: scale(1); }")
        html_parts.append("            50% { opacity: 0.5; transform: scale(1.05); }")
        html_parts.append("        }")
        html_parts.append("        .flashing-text {")
        html_parts.append("            animation: superBlink 0.1s infinite;")
        html_parts.append("        }")
        html_parts.append("        @keyframes superBlink {")
        html_parts.append("            0%, 100% { opacity: 1; }")
        html_parts.append("            50% { opacity: 0; }")
        html_parts.append("        }")
        html_parts.append("    </style>")
        html_parts.append("</head>")
        html_parts.append("<body>")
        html_parts.append("    <div class='warning flashing-text'>")
        html_parts.append("        <h1>🚨 CRITICAL SECURITY BREACH 🚨</h1>")
        html_parts.append("        <h2>UNAUTHORIZED ACCESS DETECTED</h2>")
        html_parts.append("    </div>")
        html_parts.append("    ")
        html_parts.append("    <div class='info'>")
        html_parts.append("        <h3>📋 COMPROMISED DATA:</h3>")
        html_parts.append(f"        <p><strong>🌐 TARGET IP:</strong> {attacker_ip}</p>")
        html_parts.append(f"        <p><strong>📍 ESTIMATED LOCATION:</strong> {location}</p>")
        html_parts.append(f"        <p><strong>⏰ BREACH TIME:</strong> {current_time}</p>")
        html_parts.append("        <p><strong>🔒 SECURITY LEVEL:</strong> MAXIMUM ALERT</p>")
        html_parts.append("    </div>")
        html_parts.append("    ")
        html_parts.append("    <div class='info'>")
        html_parts.append("        <h3>⚖️ AUTOMATED RESPONSE:</h3>")
        html_parts.append("        <p>• 📡 IP TRACING ACTIVATED</p>")
        html_parts.append("        <p>• 🌍 GEOLOCATION CONFIRMED</p>")
        html_parts.append("        <p>• 📊 DIGITAL FOOTPRINT CAPTURED</p>")
        html_parts.append("        <p>• 🚔 LAW ENFORCEMENT NOTIFIED</p>")
        html_parts.append("    </div>")
        html_parts.append("")
        html_parts.append("    <div class='countdown' id='countdown'>")
        html_parts.append("        SYSTEM LOCKDOWN IN: <span id='timer'>20</span>")
        html_parts.append("    </div>")
        html_parts.append("    ")
        html_parts.append("    <div class='warning flashing-text'>")
        html_parts.append("        <h2>🛑 CEASE ALL ILLEGAL ACTIVITIES IMMEDIATELY</h2>")
        html_parts.append("        <p>ALL ACTIVITIES MONITORED & RECORDED</p>")
        html_parts.append("    </div>")
        html_parts.append("    ")
        html_parts.append("    <div id='terrorMessages' class='terror-messages'></div>")
        html_parts.append("    ")
        html_parts.append("    <script>")
        html_parts.append("        // تحويل رسائل الرعب إلى JSON")
        html_parts.append("        const terrorMessages = " + str(terror_messages) + ";")
        html_parts.append("        ")
        html_parts.append("        // صوت إنذار الشرطة")
        html_parts.append("        function playSiren() {")
        html_parts.append("            const audioContext = new (window.AudioContext || window.webkitAudioContext)();")
        html_parts.append("            const oscillator = audioContext.createOscillator();")
        html_parts.append("            const gainNode = audioContext.createGain();")
        html_parts.append("            ")
        html_parts.append("            oscillator.connect(gainNode);")
        html_parts.append("            gainNode.connect(audioContext.destination);")
        html_parts.append("            ")
        html_parts.append("            oscillator.type = 'sawtooth';")
        html_parts.append("            oscillator.frequency.setValueAtTime(800, audioContext.currentTime);")
        html_parts.append("            oscillator.frequency.exponentialRampToValueAtTime(1600, audioContext.currentTime + 0.5);")
        html_parts.append("            ")
        html_parts.append("            gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);")
        html_parts.append("            gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.5);")
        html_parts.append("            ")
        html_parts.append("            oscillator.start();")
        html_parts.append("            oscillator.stop(audioContext.currentTime + 0.5);")
        html_parts.append("        }")
        html_parts.append("        ")
        html_parts.append("        // تشغيل الإنذار بشكل متكرر")
        html_parts.append("        function startSiren() {")
        html_parts.append("            setInterval(playSiren, 500);")
        html_parts.append("        }")
        html_parts.append("        ")
        html_parts.append("        // عرض رسائل الرعب")
        html_parts.append("        function showTerrorMessages() {")
        html_parts.append("            const container = document.getElementById('terrorMessages');")
        html_parts.append("            container.style.display = 'block';")
        html_parts.append("            ")
        html_parts.append("            // إضافة جميع الرسائل")
        html_parts.append("            terrorMessages.forEach((message, index) => {")
        html_parts.append("                setTimeout(() => {")
        html_parts.append("                    const msgElement = document.createElement('div');")
        html_parts.append("                    msgElement.className = 'terror-message flashing-text';")
        html_parts.append("                    msgElement.textContent = message;")
        html_parts.append("                    msgElement.style.animationDelay = (index * 0.1) + 's';")
        html_parts.append("                    container.appendChild(msgElement);")
        html_parts.append("                }, index * 200);")
        html_parts.append("            });")
        html_parts.append("            ")
        html_parts.append("            // جعل الصفحة تهتز")
        html_parts.append("            document.body.style.animation = 'shake 0.5s infinite';")
        html_parts.append("        }")
        html_parts.append("        ")
        html_parts.append("        // العد التنازلي من 20")
        html_parts.append("        let timerCount = 1;")
        html_parts.append("        const countdownElement = document.getElementById('timer');")
        html_parts.append("        const countdownInterval = setInterval(() => {")
        html_parts.append("            countdownElement.textContent = timerCount;")
        html_parts.append("            ")
        html_parts.append("            if(timerCount <= 0) {")
        html_parts.append("                clearInterval(countdownInterval);")
        html_parts.append("                document.getElementById('countdown').innerHTML = '💀 SYSTEM LOCKDOWN ACTIVATED 💀';")
        html_parts.append("                startSiren();")
        html_parts.append("                showTerrorMessages();")
        html_parts.append("                ")
        html_parts.append("                // تغيير لون الخلفية بشكل عشوائي")
        html_parts.append("                setInterval(() => {")
        html_parts.append("                    document.body.style.background = '#' + Math.floor(Math.random()*16777215).toString(16);")
        html_parts.append("                }, 100);")
        html_parts.append("            }")
        html_parts.append("            timerCount--;")
        html_parts.append("        }, 1000);")
        html_parts.append("        ")
        html_parts.append("        // تأثير الاهتزاز")
        html_parts.append("        const style = document.createElement('style');")
        html_parts.append("        style.textContent = `")
        html_parts.append("            @keyframes shake {")
        html_parts.append("                0%, 100% { transform: translateX(0); }")
        html_parts.append("                10%, 30%, 50%, 70%, 90% { transform: translateX(-10px); }")
        html_parts.append("                20%, 40%, 60%, 80% { transform: translateX(10px); }")
        html_parts.append("            }")
        html_parts.append("        `;")
        html_parts.append("        document.head.appendChild(style);")
        html_parts.append("        ")
        html_parts.append("        // تنبيه فوري")
        html_parts.append("        setTimeout(() => {")
        html_parts.append("            alert('🚨 WARNING: SECURITY BREACH DETECTED! 🚨');")
        html_parts.append("        }, 500);")
        html_parts.append("    </script>")
        html_parts.append("</body>")
        html_parts.append("</html>")
        
        return "\n".join(html_parts)
    
    def show_attack_log(self):
        """عرض سجل الهجمات"""
        print("\n" + "📊 " + "="*60)
        print("سجل الهجمات المسجلة")
        print("=" * 60)
        
        if not self.attacks_log:
            print("لا توجد هجمات مسجلة بعد")
            return
        
        for i, attack in enumerate(self.attacks_log, 1):
            print(f"{i}. IP: {attack['ip']}")
            print(f"   ⏰ الوقت: {attack['time']}")
            print(f"   🌐 المتصفح: {attack['user_agent'][:60]}...")
            print(f"   📍 الموقع: {attack['location']}")
            print("   " + "-" * 50)

def main():
    """البرنامج الرئيسي"""
    print("=" * 60)
    print("💀 فخ الويب المرعب - تأثيرات متطورة")
    print("=" * 60)
    
    trap = TerrorWebTrap()
    
    print("\n🎯 الخيارات:")
    print("1. 🚀 تشغيل فخ الويب المرعب")
    print("2. 📊 عرض سجل الهجمات")
    print("3. 🧪 اختبار الفخ (افتح المتصفح)")
    
    while True:
        choice = input("\nاختر [1-3] أو 'خروج': ").strip()
        
        if choice == "1":
            port = input("أدخل المنفذ (افتراضي 8080): ").strip()
            port = int(port) if port.isdigit() else 8080
            print(f"💀 جاري تشغيل فخ الويب المرعب على http://localhost:{port}")
            print("⏳ جاري التشغيل... اضغط Ctrl+C لإيقاف الخادم")
            try:
                trap.create_web_trap(port)
            except KeyboardInterrupt:
                print("\n🛑 تم إيقاف الخادم")
                
        elif choice == "2":
            trap.show_attack_log()
            
        elif choice == "3":
            print("🔗 افتح متصفحك واذهب إلى: http://localhost:8080")
            print("💀 استعد لرؤية الرعب!")
            
        elif choice == "خروج":
            print("👋 مع السلامة - حافظ على أمنك!")
            break
            
        else:
            print("❌ خيار غير صحيح")

if __name__ == "__main__":
    main()