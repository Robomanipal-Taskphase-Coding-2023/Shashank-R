#include<iostream>
#include<vector>
#include<algorithm>
#include<cstddef>

using namespace std;

int main()
{
    constexpr size_t M = 3;
    constexpr size_t N = 3;
    int matrix[M][N] = {
        {1, 2, 3},
        {0, 4, 5},
        {4, 2, 0}
    };

    vector<size_t> markedRows;
    vector<size_t> markedColumns;
    for (size_t ii = 0; ii < M; ++ii) {
        for(size_t jj = 0; jj < N; ++jj) {
            if (matrix[ii][jj] == 0) {
                markedRows.push_back   (ii);
                markedColumns.push_back(jj);
            }
        }
    }
    sort(markedColumns.begin(),markedColumns.end());
    markedRows.erase   (unique(markedRows.begin()   ,markedRows.end())   ,markedRows.end()   );
    markedColumns.erase(unique(markedColumns.begin(),markedColumns.end()),markedColumns.end());

    vector<size_t> irow;
    vector<size_t> icol;
    vector<int>    val;
    for (size_t ii = 0; ii < M; ++ii) {
        for(size_t jj = 0; jj < N; ++jj) {
            if ( ( find(markedRows.begin()   ,markedRows.end()   ,ii) == markedRows.end()    ) &&
                 ( find(markedColumns.begin(),markedColumns.end(),jj) == markedColumns.end() )
                ) {
                  irow.push_back(ii);
                  icol.push_back(jj);
                  val.push_back (matrix[ii][jj]);
                }
        }
    }
