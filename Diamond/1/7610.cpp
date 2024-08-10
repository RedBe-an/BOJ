#include <bits/stdc++.h>
#define x first
#define y second
#define all(v) v.begin(), v.end()
#define compress(v) sort(all(v)), v.erase(unique(all(v)), v.end())
using namespace std;

typedef long long ll;

struct Node{
    Node *l, *r, *p; int val;
    Node() : Node(1) {}
    Node(int val) : l(nullptr), r(nullptr), p(nullptr), val(val) {}
    bool IsLeft() const { return this == p->l; }
    bool IsRoot() const { return !p || (p->l != this && p->r != this); }
    void Rotate(){
        if(IsRoot()) return;
        if(IsLeft()){
            if(r) r->p = p; p->l = r; r = p;
        }
        else{
            if(l) l->p = p; p->r = l; l = p;
        }
        if(!p->IsRoot()) (p->IsLeft() ? p->p->l : p->p->r) = this;
        auto t = p; p = t->p; t->p = this;
    }
};
void Splay(Node *x){
    for(; !x->IsRoot(); x->Rotate()){
        if(!x->p->IsRoot()){
            if(x->IsLeft() == x->p->IsLeft()) x->p->Rotate();
            else x->Rotate();
        }
    }
}
void Access(Node *x){
    Splay(x); x->r = nullptr;
    for(; x->p; Splay(x)) Splay(x->p), x->p->r = x;
}
void link(Node *p, Node *c){
    Access(c); Access(p);
    c->l = p; p->p = c;
}
void Cut(Node *x){
    Access(x); x->l->p = nullptr; x->l = nullptr;
}
Node* Root(Node *x){
    Access(x); while(x->l) x = x->l;
    Access(x); return x;
}
Node* Par(Node *x){
    Access(x); if(!x->l) return nullptr;
    x = x->l; while(x->r) x = x->r;
    Access(x); return x;
}

int N, M, Q;
int X[202020], Y[202020];

Node nd[202020];
bool chk[202020];
int sum[202020];

void On(int t){
    int a = Root(nd + X[t]) - nd;
    int b = Root(nd + Y[t]) - nd;
    int now = nd[a].val + nd[b].val - sum[t];
    link(nd + X[t], nd + Y[t]);
    a = Root(nd + X[t]) - nd;
    nd[a].val = now;
}
void Off(int t){
    int a = X[t], b = Y[t];
    int rt = Root(nd + a) - nd;
    int now = nd[rt].val;
    if(Par(nd + a) - nd == b) Cut(nd + a);
    else Cut(nd + b);
    sum[t] = now;
    a = Root(nd + a) - nd;
    b = Root(nd + b) - nd;
    nd[a].val = nd[b].val = now;
}

int main(){
    ios_base::sync_with_stdio(false); cin.tie(nullptr);
    cin >> N >> M >> Q;
    for(int i=1; i<N; i++) cin >> X[i] >> Y[i];
    for(int i=1; i<=M; i++){
        int t; cin >> t; chk[t] ^= 1;
        if(chk[t]) On(t);
        else Off(t);
    }
    for(int i=1; i<=Q; i++){
        int t; cin >> t;
        int rt = Root(nd + t) - nd;
        cout << nd[rt].val << "\n";
    }
}