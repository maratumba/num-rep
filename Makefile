build-amd:
	docker build . --platform linux/amd64 -t cnr-test:latest-amd64

build-amd-mkl:
	docker build . -f Dockerfile-mkl --platform linux/amd64 -t cnr-test-mkl:latest-amd64

build-arm:
	docker build . --platform linux/arm64 -t cnr-test:latest-arm64

build-native:
	docker build . -t cnr-test:latest

build: build-amd build-arm build-amd-mkl

.SILENT: calc-score
calc-score:
	echo 'host\tarm64\tamd64' > output/combined_results.txt; \
	paste output/result.txt output/result-arm64.txt output/result-amd64.txt >> output/combined_results.txt; \
	echo 'host\t\tarm64\t\tamd64'
	paste output/result.txt output/result-arm64.txt output/result-amd64.txt | tail -n 10
	python calc_score.py output/result.txt output/result-arm64.txt output/result-amd64.txt > output/scores.txt
	cat output/scores.txt

docker-run-arm64:
	docker run --platform linux/arm64 -v ./output:/app/output cnr-test:latest-arm64 python test_cnr.py ./output/result-arm64.txt ./output/arm64_platform.json; \

docker-run-mkl-amd64:
	docker run --platform linux/amd64 -v ./output:/app/output cnr-test-mkl:latest-amd64 python test_cnr.py ./output/result-mkl-amd64.txt ./output/amd64-mkl_platform.json;

docker-run-amd64:
	docker run --platform linux/amd64 -v ./output:/app/output cnr-test:latest-amd64 python test_cnr.py ./output/result-amd64.txt ./output/amd64_platform.json;

docker-run: docker-run-arm64 docker-run-amd64 docker-run-mkl-amd64
	python test_cnr.py output/result.txt output/native_platform.json; \

.SILENT: run
run: docker-run calc-score
