import { createStore } from 'vuex';

export default createStore({
  state: {
    isAuthenticated: false,
    accessToken: null,
    refreshToken: null,
    tokenExpiration: null,
  },
  mutations: {
    setAuthentication(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
    setAccessToken(state, accessToken) {
        state.accessToken = accessToken;
        localStorage.setItem('accessToken', accessToken);
    },
    setRefreshToken(state, refreshToken) {
        state.refreshToken = refreshToken;
        localStorage.setItem('refreshToken', refreshToken);
    },
    setTokenExpiration(state, tokenExpiration) {
        state.tokenExpiration = tokenExpiration;
        localStorage.setItem('tokenExpiration', tokenExpiration)
    }
  },
});
