<template>
  <div class="ktp-button">
    <my-section>
      <template v-slot:title>基础</template>
      <!-- <template v-slot:desc>由于选项默认可见，不宜过多，若选项过多，建议使用 Select 选择器。</template> -->
      <el-input v-model="input" placeholder="请输入内容"></el-input>
    </my-section>

    <my-section>
      <template v-slot:title>限数字</template>
      <template v-slot:desc>使用<code>type="number"</code>属性即可</template>
      <el-input placeholder="请输入内容" onpaste="return false" type="number" @keypress="press" v-model="number"></el-input>
    </my-section>

    <my-section>
      <template v-slot:title>限正数或2位小数</template>
      <!-- <template v-slot:desc>使用<code>type="number"</code>属性即可</template> -->
      <el-input placeholder="请输入内容" type="number" onpaste="return false" v-model="integer" @keypress="press" @keyup="keyup"></el-input>
    </my-section>

    <my-section>
      <template v-slot:title>限长度</template>
      <template v-slot:desc>使用<code>maxlength</code>属性即可，此处<code>maxlength</code>等于<el-input class="maxlength" type="number" size="mini" v-model="maxlength" placeholder="请输入限制长度" /></template>
      <el-input placeholder="请输入内容" :maxlength="maxlength" v-model="maxlengthValue"></el-input>
    </my-section>

    <my-section>
      <template v-slot:title>密码框</template>
      <template v-slot:desc>使用<code>show-password</code>属性即可得到一个可切换显示隐藏的密码框</template>
      <el-input placeholder="请输入密码" v-model="password" show-password></el-input>
    </my-section>

    <my-section>
      <template v-slot:title>手机号码校验</template>
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="0">
        <el-form-item label="" prop="phone">
          <el-input placeholder="请输入手机号码" v-model="ruleForm.phone"></el-input>
        </el-form-item>
      </el-form>
    </my-section>

    <my-section>
      <template v-slot:title>身份证校验</template>
      <el-form :model="ruleForm" :rules="rules" label-width="0">
        <el-form-item label="" prop="idCard">
          <el-input placeholder="请输入身份证号码" v-model="ruleForm.idCard"></el-input>
        </el-form-item>
      </el-form>
    </my-section>

    <my-section>
      <template v-slot:title>统一社会信用代码校验</template>
      <el-form :model="ruleForm" :rules="rules" label-width="0">
        <el-form-item label="" prop="creditCode">
          <el-input placeholder="请输入统一社会信用代码" v-model="ruleForm.creditCode"></el-input>
        </el-form-item>
      </el-form>
    </my-section>

    <my-section>
      <template v-slot:title>文本框</template>
      <template v-slot:desc>用于输入多行文本信息，通过将 type 属性的值指定为<code>textarea</code>。</template>
      <el-input
        type="textarea"
        :rows="textarea.row"
        placeholder="请输入内容"
        :maxlength="textarea.maxlength"
        :show-word-limit="textarea.show"
        resize="none"
        v-model="textarea.value">
      </el-input>
      <p class="tip">通过将设置<code>row</code>属性控制文本域高度。<el-input-number size="mini" v-model="textarea.row" :min="1" label="请输入row的值"></el-input-number></p>
      
      <p class="tip">通过将设置<code>autosize</code>属性可以使得文本域的高度能够根据文本内容自动进行调整，并且<code>autosize</code>还可以设定为一个对象<code>{ minRows: 2, maxRows: 4}</code>，指定最小行数和最大行数。</p>
      <p><code>maxlength</code>和<code>minlength</code>是原生属性，用来限制输入框的字符长度，其中字符长度是用 Javascript 的字符串长度统计的。对于类型为<code>text</code>或<code>textarea</code>的输入框，在使用<code>maxlength</code>属性限制最大输入长度的同时，可通过设置<code>show-word-limit</code>属性来展示字数统计。</p>
      <el-input size="mini" type="number" min="0" v-model="textarea.maxlength" placeholder="文本框最大输入长度" />
      <el-switch v-model="textarea.show" active-text="显示" style="margin-left: 10px" />
    </my-section>
    
  </div>
</template>

<script>
export default {
  data () {
    const validatePhone = function (rule, value, callback) {
      if (value === '') {
        callback(new Error('手机号码不能为空！'));
      } else {
        const re = /^1[3|4|5|7|8][0-9]{9}$/
        if (!re.test(value)) {
          callback(new Error('手机号码格式错误！'));
        }
        callback();
      }
    }
    const validateIdCard = function (rule, value, callback) {
      if (value === '') {
        callback(new Error('身份证号码不能为空！'));
      } else {
        const re = /^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$|^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}([0-9]|X)$/
        if (!re.test(value)) {
          callback(new Error('身份证号码格式错误！'));
        }
        callback();
      }
    }
    const validateCreditCode = function (rule, value, callback) {
      if (value === '') {
        callback(new Error('统一社会信用代码不能为空！'));
      } else {
        const re = /^([0-9A-HJ-NPQRTUWXY]{2}\d{6}[0-9A-HJ-NPQRTUWXY]{10}|[1-9]\d{14})$/
        if (!re.test(value)) {
          callback(new Error('统一社会信用代码格式错误！'));
        }
        callback();
      }
    }
    return {
      input: '',
      number: '',
      integer: '',
      maxlengthValue: '',
      maxlength: 16,
      password: '',
      textarea: {
        value: '',
        row: 5,
        maxlength: 500,
        show: true
      },
      ruleForm: {
        phone: '',
        idCard: '',
        creditCode: ''
      },
      rules: {
        phone: [
          { validator: validatePhone, trigger: 'blur' }
        ],
        idCard: [
          { validator: validateIdCard, trigger: 'blur' }
        ],
        creditCode: [
          { validator: validateCreditCode, trigger: 'blur' }
        ]
      }
    }
  },
  watch: {
    maxlength: function () {
      this.maxlengthValue = ''
    }
  },
  methods: {
    press (e) {
      // console.log(e)
      if (e.keyCode == 46 && !e.target.value) {
        e.target.value = ''
        e.preventDefault()
      }
    },
    keyup (e) {
      this.integer = this.integer.replace(/[^\d.]/g, '').replace(/^(\-)*(\d+)\.(\d\d).*$/, '$1$2.$3')
    }
  }
}
</script>

<style scoped>
.el-input {
  width: 220px;
}
.el-textarea {
  width: 50%;
}
.maxlength {
  margin-left: 10px;
  width: 120px;
}
</style>