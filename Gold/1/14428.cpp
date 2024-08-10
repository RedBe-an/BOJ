#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class SegmentTree {
private:
    vector<int> tree;
    vector<int> arr;
    int n;

    void build(int node, int start, int end) {
        if (start == end) {
            tree[node] = start; // leaf node will have the index
        } else {
            int mid = (start + end) / 2;
            build(2 * node, start, mid);
            build(2 * node + 1, mid + 1, end);
            // store the index of the minimum value
            if (arr[tree[2 * node]] <= arr[tree[2 * node + 1]]) {
                tree[node] = tree[2 * node];
            } else {
                tree[node] = tree[2 * node + 1];
            }
        }
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            arr[idx] = val; // update the value
            tree[node] = start; // update the index in the tree
        } else {
            int mid = (start + end) / 2;
            if (start <= idx && idx <= mid) {
                update(2 * node, start, mid, idx, val);
            } else {
                update(2 * node + 1, mid + 1, end, idx, val);
            }
            // update the minimum index
            if (arr[tree[2 * node]] <= arr[tree[2 * node + 1]]) {
                tree[node] = tree[2 * node];
            } else {
                tree[node] = tree[2 * node + 1];
            }
        }
    }

    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) {
            return -1; // out of range
        }
        if (l <= start && end <= r) {
            return tree[node]; // within range
        }
        int mid = (start + end) / 2;
        int leftIndex = query(2 * node, start, mid, l, r);
        int rightIndex = query(2 * node + 1, mid + 1, end, l, r);
        if (leftIndex == -1) return rightIndex;
        if (rightIndex == -1) return leftIndex;
        return (arr[leftIndex] <= arr[rightIndex]) ? leftIndex : rightIndex;
    }

public:
    SegmentTree(const vector<int>& input) {
        n = input.size();
        arr = input;
        tree.resize(4 * n);
        build(1, 0, n - 1);
    }

    void update(int idx, int val) {
        update(1, 0, n - 1, idx, val);
    }

    int query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int N;
    cin >> N;
    vector<int> A(N);
    for (int i = 0; i < N; ++i) {
        cin >> A[i];
    }

    SegmentTree segTree(A);

    int M;
    cin >> M;
    for (int i = 0; i < M; ++i) {
        int type;
        cin >> type;
        if (type == 1) {
            int idx, val;
            cin >> idx >> val;
            segTree.update(idx - 1, val); // 1-based to 0-based index
        } else if (type == 2) {
            int l, r;
            cin >> l >> r;
            int minIndex = segTree.query(l - 1, r - 1); // 1-based to 0-based index
            cout << minIndex + 1 << '\n'; // output in 1-based index
        }
    }

    return 0;
}
