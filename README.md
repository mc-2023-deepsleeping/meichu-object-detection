# meichu-object-detection
### Requirements
python <= 3.10
```bash
conda create --name meichu
conda activate meichu
pip install -r requirements.txt
```
### Training
```bash
python .\train.py --weights .\cur_model.pt --cfg .\cfg\training\yolov7.yaml --hyp .\data\hyp.scratch.custom.yaml --epochs 100 --batch-size 1 --device 0 --data ./datasets/customdataset.yaml --save_period 5
```

### Testing 

### Testing (w/ flask as backend)