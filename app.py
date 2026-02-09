from Flask_project import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
# host='0.0.0.0', port=5000, debug=False（如果需要服务器部署到公网就放这个）