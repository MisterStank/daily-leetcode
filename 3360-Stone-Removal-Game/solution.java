class Solution {
    public boolean canAliceWin(int n) {
        boolean alice_win = false;
        int remove = 10;
        while (n > 0){
            n -= remove;
            if (n >= 0)
                alice_win = !alice_win;
            remove--;
        }
        return alice_win;
    }
}