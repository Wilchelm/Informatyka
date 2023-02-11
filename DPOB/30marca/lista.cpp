#include "lista.h"

template <class T> 
Lista<T>::Lista() {
        _rozmiar = 0;
}

template <class T>
void Lista<T>::wstawElement(T element) {
        _dane[_rozmiar++] = element;
}

template <class T>
T Lista<T>::podajElement(int index) {
        return _dane[index];
}
