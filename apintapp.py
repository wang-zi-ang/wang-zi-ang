from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Paint Tool</title>
    <style>
        canvas { border: 1px solid #000; }
    </style>
</head>
<body>
    <h2>Paint Tool</h2>
    <canvas id="paint" width="800" height="600"></canvas>
    <script>
        const canvas = document.getElementById('paint');
        const ctx = canvas.getContext('2d');
        let painting = false;

        canvas.addEventListener('mousedown', () => { painting = true; });
        canvas.addEventListener('mouseup', () => { painting = false; ctx.beginPath(); });
        canvas.addEventListener('mousemove', draw);

        function draw(e) {
            if (!painting) return;
            ctx.lineWidth = 2;
            ctx.lineCap = 'round';
            ctx.strokeStyle = 'black';

            ctx.lineTo(e.offsetX, e.offsetY);
            ctx.stroke();
            ctx.beginPath();
            ctx.moveTo(e.offsetX, e.offsetY);
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)