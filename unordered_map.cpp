#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <algorithm>
#include <utility>
#include <list>
#include <stdexcept>

using std::vector;
using std::string;
using std::pair;
using std::list;

const int map_size = 100007;

template<class KeyType, class ValueType, class Hash = std::hash<KeyType>> class HashMap {
 public:
    typedef pair<const KeyType, ValueType> Pairs;

    HashMap() {
        map_.resize(map_size);
        hasher_ = Hash();
    }

    HashMap(Hash hasher) : hasher_(hasher) {
        map_.resize(map_size);
    }

    template<typename InputIterator>
    HashMap(InputIterator begin,
            InputIterator end,
            Hash hasher = Hash()) : hasher_(hasher) {
        map_.resize(map_size);
        for (; begin != end; ++begin) {
            insert(*begin);
        }
    }

    HashMap(std::initializer_list<Pairs> data, Hash hasher = Hash()) : hasher_(hasher) {
        map_.resize(map_size);
        for (auto it = data.begin(); it != data.end(); ++it) {
            insert(*it);
        }
    }

    size_t size() const {
        return data_.size();
    }

    bool empty() const {
        return data_.empty();
    }

    Hash hash_function() const {
        return hasher_;
    }

    void insert(Pairs Pair) {
        if (find(Pair.first) == end()) {
            data_.push_back(Pair);
            auto it = end();
            --it;
            map_[hasher_(Pair.first) % map_size].push_back(it);
        }
    }

    void erase(const KeyType key) {
        auto elem_it = find(key);
        if (elem_it != end()) {
            auto tmp = elem_it;
            map_[hasher_(key) % map_size].remove(elem_it);
            data_.erase(tmp);
        }
    }

    using iterator = typename list<pair<const KeyType, ValueType>>::iterator;
    using const_iterator = typename list<pair<const KeyType, ValueType>>::const_iterator;

    typename list<Pairs>::const_iterator begin() const {
        return data_.cbegin();
    }

    typename list<Pairs>::const_iterator end() const {
        return data_.cend();
    }

    typename list<Pairs>::iterator begin() {
        return data_.begin();
    }

    typename list<Pairs>::iterator end() {
        return data_.end();
    }

    typename list<Pairs>::iterator find(const KeyType key) {
        auto it = map_[hasher_(key) % map_size].begin();
        for (; it != map_[hasher_(key) % map_size].end(); ++it) {
            if ((*it)->first == key) {
                return *it;
            }
        }
        return data_.end();
    }

    typename list<Pairs>::const_iterator find(const KeyType key) const {
        auto it = map_[hasher_(key) % map_size].begin();
        for (; it != map_[hasher_(key) % map_size].end(); ++it) {
            if ((*it)->first == key) {
                return *it;
            }
        }
        return data_.cend();
    }

    ValueType& operator[](const KeyType key) {
        auto it = find(key);
        if (it != end()) {
            return it->second;
        } else {
            insert(std::make_pair(key, ValueType()));
            it = find(key);
            return it->second;
        }
    }

    const ValueType& at(const KeyType key) const {
        auto it = find(key);
        if (it != end()) {
            return it->second;
        } else {
            throw std::out_of_range(" ");
        }
    }

    void clear() {
        for (auto it = data_.begin(); it != data_.end(); ++it) {
            map_[hasher_(it->first) % map_size].pop_back();
        }
        data_.clear();
    }

    HashMap<KeyType, ValueType, Hash> & operator=(HashMap<KeyType, ValueType, Hash>& map) {
        HashMap<KeyType, ValueType, Hash> temp(map.begin(), map.end());
        temp.swap(*this);
        return *this;
    }

    HashMap<KeyType, ValueType, Hash> & operator=(const HashMap<KeyType, ValueType, Hash>& map) {
        HashMap<KeyType, ValueType, Hash> temp(map.begin(), map.end());
        temp.swap(*this);
        return *this;
    }

    void swap(HashMap<KeyType, ValueType, Hash>& map) throw() {
        std::swap(this->data_, map.data_);
        std::swap(this->map_, map.map_);
        std::swap(this->hasher_, map.hasher_);
    }

 private:
    list<Pairs> data_;
    vector<list<typename list<Pairs>::iterator>> map_;
    Hash hasher_;
};
