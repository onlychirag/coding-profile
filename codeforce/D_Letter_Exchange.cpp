# include <bits/stdc++.h>
# define ll long long
# define all(x) x.begin(),x.end()

using namespace std;

struct op{
    int a , b ;
    char aa , bb ;
    op( int _a , char _aa , int _b , char _bb ) : a(_a) , aa(_aa) , b(_b) , bb(_bb) {}
};

void solve() {
    int n ; cin >> n ;
    vector<op> ans ;
    map<pair<char,char>,set<int>> mp ;
    for (int i = 0; i < n; ++i) {
        string s ; cin >> s ;
        sort(all(s)) ;
        if ( s == "www" ){
            mp[{'w','i'}].insert(i+1) ;
            mp[{'w','n'}].insert(i+1) ;
        }else if ( s == "iii" ){
            mp[{'i','w'}].insert(i+1) ;
            mp[{'i','n'}].insert(i+1) ;
        }else if ( s == "nnn" ){
            mp[{'n','w'}].insert(i+1) ;
            mp[{'n','i'}].insert(i+1) ;
        }else{
            if ( s == "iiw" ){
                mp[{'i','n'}].insert(i+1) ;
            }else if ( s == "iin" ){
                mp[{'i','w'}].insert(i+1) ;
            }else if ( s == "nnw" ){
                mp[{'n','i'}].insert(i+1) ;
            }else if ( s == "inn" ){
                mp[{'n','w'}].insert(i+1) ;
            }else if ( s == "nww" ){
                mp[{'w','i'}].insert(i+1) ;
            }else if ( s == "iww" ){
                mp[{'w','n'}].insert(i+1) ;
            }
        }
    }
    auto rev = [&]( pair<char,char> a ){
        return make_pair(a.second,a.first) ;
    };
    auto bad = [&]( pair<char,char> a ){
        char from = a.second , to ;
        if ( from == 'w' )
            to = ( a.first == 'i' ? 'n' : 'i' ) ;
        else if ( from == 'i' )
            to = ( a.first == 'w' ? 'n' : 'w' ) ;
        else
            to = ( a.first == 'i' ? 'w' : 'i' ) ;
        return make_pair(from,to) ;
    };
    for ( auto &it : mp ){
        auto &st = it.second ;
        while ( !st.empty() ){
            auto cur = *st.begin() ;
            if ( !mp[rev(it.first)].empty() ){
                ans.push_back(op(cur,it.first.first, *mp[rev(it.first)].begin(), it.first.second)) ;
                mp[rev(it.first)].erase(mp[rev(it.first)].begin());
                st.erase(cur) ;
            }else{
                break;
            }
        }
        while ( !st.empty() ){
            auto cur = *st.begin() ;
            if ( !mp[bad(it.first)].empty() ){
                ans.push_back(op(cur,it.first.first, *mp[bad(it.first)].begin(), it.first.second)) ;
                int id = *mp[bad(it.first)].begin();
                st.erase(cur) ;
                mp[bad(it.first)].erase(id);
                mp[ { it.first.first , bad(it.first).second } ].insert(id) ;
            }
        }
    }
    for ( auto &it : mp ){
        auto &st = it.second ;
        while ( !st.empty() ){
            auto cur = *st.begin() ;
            st.erase(cur) ;
            if ( !mp[rev(it.first)].empty() ){
                ans.push_back(op(cur,it.first.first, *mp[rev(it.first)].begin(), it.first.second)) ;
                mp[rev(it.first)].erase(mp[rev(it.first)].begin());
            }else{
                break;
            }
        }
        while ( !st.empty() ){
            auto cur = *st.begin() ;
            st.erase(cur) ;
            if ( !mp[bad(it.first)].empty() ){
                ans.push_back(op(cur,it.first.first, *mp[bad(it.first)].begin(), it.first.second)) ;
                int id = *mp[bad(it.first)].begin();
                mp[bad(it.first)].erase(id);
                mp[ { it.first.second , bad(it.first).second } ].insert(id) ;
            }
        }
    }
    cout << ans.size() << '\n' ;
    for ( auto &ele : ans )
        cout << ele.a << ' ' << ele.aa << ' ' << ele.b << ' ' << ele.bb << '\n' ;
}

int main() {
    cin.tie(nullptr), cout.tie(nullptr), iostream::sync_with_stdio(false) ;
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
    int t = 1; cin >> t ;
    while (t--)
        solve();
    return 0;
}