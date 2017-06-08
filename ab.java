class AB {

   public String createString(int N, int K){
            StringBuffer ab = new StringBuffer(N);
            for (int i = 0; i < N; i++){
               ab.append("B");
            }
            int currentK = 0;
            int currentNewAindex = 0;
            int diff = K-N;  //''' 12 - 10 = 2 '''  ''' 6-5 = 1''''
            int previousA = 0;

            for(int i = 1; i <= diff; i++) {
                previousA = this.findMaxIndex(currentNewAindex,currenK, previousA);
                ab[previousA] = A;

                if(currenK > K) {
                    // "N characters is too short for this value of K."
                    ab = "";
                    break;
                }
            }

           	return ab.toString();
    }

    private int findMaxIndex(int currentNewAindex, int currenK, int previousA){
        currenK = currenK+N-1-currentNewAindex;
        while ( currenK > K && currentNewAindex > previousA) {
          currentNewAindex--;
        }

        return currentNewAindex;
	}
}
