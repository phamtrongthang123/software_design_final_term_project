flask_server

## Dependencies

```
pip install -r requirements.txt
```

## Start server

### Local
```
cd flask_server
python app.py
```
### Google colab
```
cd flask_server
python app_colab.py
```
### With docker
Require aws: at least 2 cpu cores, 2gb RAM.
```
sudo docker build -t flask_server .
sudo docker run -i -t  -p 3000:3000 flask_server:latest /bin/bash
```
if it didnt start, go into the bash of docker and run manually 
```
python app.py
```

## Return value

POST form has to be:

```
mydata = {'img_encoded': base64_string, 'lang': 'custom', 'type': 'classify'}
```

type is classify / detection

Return value:

```
#classify
{'type':'classify', 'size': [img.width, img.height], "predicted": classes[predicted], "score": score.item()}

#detection
{'type': 'detection', 'size': [img.width, img.height], "predicted": base64_string}
```

## Example call API

### VNLang (WIP)

```vnlang
// http.vnl
in_ra("Đây là ví dụ dùng lib http")
đặt http = sử_dụng("../library/libhttp.vnl")
http.req_post("http://127.0.0.1:3000/cifar_classifier","./imgs/palm.jpg")
```

```
cd example
go run ../src/vnlang/main.go http.vnl
```
