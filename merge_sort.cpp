#include <iostream>
#include <memory>

using std::shared_ptr;

class Elem {
 public:
     int elem_;
     shared_ptr<Elem> ptr_;
     Elem() : elem_(0), ptr_(nullptr)
     {}

     Elem(int elem) : elem_(elem), ptr_(nullptr)
     {}

     void operator = (Elem& a) {
        elem_ = a.elem_;
        ptr_ = a.ptr_;
        return;
     }
};

class List {
 public:
     shared_ptr<Elem> root_;
     shared_ptr<Elem> head_;
     int length_ = 0;
     List() : root_(shared_ptr<Elem>(new Elem())), head_(shared_ptr<Elem>(new Elem()))
     {}

     void add(int elem) {
        if (length_ == 0) {
            root_->elem_ = elem;
            head_ = root_;
            ++length_;
        } else {
            shared_ptr<Elem> ptr (new Elem(elem));
            head_->ptr_ = ptr;
            head_ = ptr;
            ++length_;
        }
     }
};

shared_ptr<Elem> middle(shared_ptr<Elem> left, int length) {
    for (int i = 0; i != (length - 1) / 2; ++i) {
        left = left->ptr_;
    }
    return left;
}

void Merge(List &data, shared_ptr<Elem> left, shared_ptr<Elem> middle, shared_ptr<Elem> right) {
    List ans;
    auto i = left;
    auto j = middle->ptr_;
    while (i != middle->ptr_ && j != right->ptr_) {
        if (i->elem_ < j->elem_) {
            ans.add(i->elem_);
            i = i->ptr_;
        } else {
            ans.add(j->elem_);
            j = j->ptr_;
        }
    }
    while (i != middle->ptr_) {
        ans.add(i->elem_);
        i = i->ptr_;
    }
    while (j != right->ptr_) {
        ans.add(j->elem_);
        j = j->ptr_;
    }
    auto listb = left;
    auto ansb = ans.root_;
    while (ansb != nullptr) {
        listb->elem_ = ansb->elem_;
        listb = listb->ptr_;
        ansb = ansb->ptr_;
    }
}

void MergeSort(List &data, shared_ptr<Elem> left, shared_ptr<Elem> right, int length) {
    if (length > 1) {
        auto mid = middle(left, length);
        MergeSort(data, left, mid, length - length / 2);
        MergeSort(data, mid->ptr_, right, length / 2);
        Merge(data, left, mid, right);
    }
}

int main() {
    int length;
    std::cin >> length;
    List input;
    int tmp;
    for (int i = 0; i != length; ++i) {
        std::cin >> tmp;
        input.add(tmp);
    }
    MergeSort(input, input.root_, input.head_, length);
    for (int i = 0; i != length; ++i) {
        std::cout << (input.root_)->elem_ << " ";
        input.root_ = input.root_->ptr_;
    }
}
