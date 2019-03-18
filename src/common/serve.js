import axios from 'axios';
import qs from 'qs';

class Http {
  constructor() {
    this.ins = axios.create({
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    });
  }

  get(url, param = {}, config = {}) {
    config.params = param;
    return this.ins.get(url, config);
  }

  post(url, data = {}, config = {}) {
    return this.ins.post(url, qs.stringify(data), config);
  }

  delete(url, param = {}, config = {}) {
    config.params = param;
    return this.ins.delete(url, config);
  }

  put(url, body = {}, config = {}) {
    return this.ins.put(url, body, config);
  }
}

const http = new Http();
export default http;
