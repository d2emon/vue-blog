<template>
  <base-form
    :form-name="formName"
    :fields="formData"
    :errors="errors"
    @submit="formSubmit"
  />
</template>

<script lang="ts">
import Vue from 'vue';
import {
  Component,
} from 'vue-property-decorator';
import {
  FormData,
} from './types';
import {
  isRequired,
} from '@/helpers/validators';

@Component({
  components: {
    BaseForm: () => import('./BaseForm.vue'),
  },
  props: {
    errors: Object,
  },
})
export default class Login extends Vue {
  formName: string = 'loginForm';

  formData: FormData = {
    username: {
      label: 'Username',
      rules: [
        isRequired('Username is required'),
      ],
      required: true,
      size: 20,
    },
    password: {
      label: 'Password',
      rules: [
        isRequired('Password is required'),
      ],
      required: true,
      size: 20,
      type: 'password',
    },
    rememberMe: {
      label: 'Remember Me',
      value: true,
      rules: [],
      isCheckBox: true,
    },
  };

  formSubmit(values: {}) {
    this.$emit('submit', values);
  }
}
</script>
