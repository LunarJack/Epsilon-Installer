all:
mac:
	$(CXX) -framework Python -std=c++20 -Iinclude src/main.cpp -c
	$(CXX) -framework Python -Llib/mac main.o -o build/installer
	mv *.o build/
linux:
win:
clean:
	rm -rf *.o
	rm -rf build/*