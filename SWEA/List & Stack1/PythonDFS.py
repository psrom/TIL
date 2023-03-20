# DFS(깊이 우선 탐색)
visited = []
stack = []

# DFS(v)
#   v 방문;
#   visited[v] <- true;
#   do {
#       if (v의 인접 정점 중 방문 안 한 w 찾기)
#           push(v);
#       while(w) {
#           w 방문;
#           visited[w] <- true;
#           push(w);
#           v<-w;
#           v의 인접 정점 중 방문 안 한 w찾기
#       }
#       v <- pop(stack);
#    }while(v)
# end DFS()