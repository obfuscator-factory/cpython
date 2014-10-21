	
code = ["" for _ in range(255)]
code[9]="""            goto fast_next_opcode;

"""
code[124]="""            x = GETLOCAL(oparg);
            if (x != NULL) {
                Py_INCREF(x);
                PUSH(x);
                goto fast_next_opcode;
            }
            format_exc_check_arg(PyExc_UnboundLocalError,
                UNBOUNDLOCAL_ERROR_MSG,
                PyTuple_GetItem(co->co_varnames, oparg));
            break;
	
"""
code[100]="""            x = GETITEM(consts, oparg);
            Py_INCREF(x);
            PUSH(x);
            goto fast_next_opcode;
	

"""
code[125]="""            v = POP();
            SETLOCAL(oparg, v);
            goto fast_next_opcode;

"""
code[1]="""            v = POP();
            Py_DECREF(v);
            goto fast_next_opcode;

"""
code[2]="""            v = TOP();
            w = SECOND();
            SET_TOP(w);
            SET_SECOND(v);
            goto fast_next_opcode;

"""
code[3]="""            v = TOP();
            w = SECOND();
            x = THIRD();
            SET_TOP(w);
            SET_SECOND(x);
            SET_THIRD(v);
            goto fast_next_opcode;

"""
code[5]="""            u = TOP();
            v = SECOND();
            w = THIRD();
            x = FOURTH();
            SET_TOP(v);
            SET_SECOND(w);
            SET_THIRD(x);
            SET_FOURTH(u);
            goto fast_next_opcode;

"""
code[4]="""            v = TOP();
            Py_INCREF(v);
            PUSH(v);
            goto fast_next_opcode;
	
"""
code[99]="""            if (oparg == 2) {
                x = TOP();
                Py_INCREF(x);
                w = SECOND();
                Py_INCREF(w);
                STACKADJ(2);
                SET_TOP(x);
                SET_SECOND(w);
                goto fast_next_opcode;
            } else if (oparg == 3) {
                x = TOP();
                Py_INCREF(x);
                w = SECOND();
                Py_INCREF(w);
                v = THIRD();
                Py_INCREF(v);
                STACKADJ(3);
                SET_TOP(x);
                SET_SECOND(w);
                SET_THIRD(v);
                goto fast_next_opcode;
            }
            Py_FatalError("invalid argument to DUP_TOPX"
                          " (bytecode corruption?)");
            /* Never returns, so don't bother to set why. */
            break;

"""
code[10]="""            v = TOP();
            x = PyNumber_Positive(v);
            Py_DECREF(v);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[11]="""            v = TOP();
            x = PyNumber_Negative(v);
            Py_DECREF(v);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[12]="""            v = TOP();
            err = PyObject_IsTrue(v);
            Py_DECREF(v);
            if (err == 0) {
                Py_INCREF(Py_True);
                SET_TOP(Py_True);
                continue;
            }
            else if (err > 0) {
                Py_INCREF(Py_False);
                SET_TOP(Py_False);
                err = 0;
                continue;
            }
            STACKADJ(-1);
            break;

"""
code[13]="""            v = TOP();
            x = PyObject_Repr(v);
            Py_DECREF(v);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[15]="""            v = TOP();
            x = PyNumber_Invert(v);
            Py_DECREF(v);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[19]="""            w = POP();
            v = TOP();
            x = PyNumber_Power(v, w, Py_None);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[20]="""            w = POP();
            v = TOP();
            x = PyNumber_Multiply(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[21]="""            if (!_Py_QnewFlag) {
                w = POP();
                v = TOP();
                x = PyNumber_Divide(v, w);
                Py_DECREF(v);
                Py_DECREF(w);
                SET_TOP(x);
                if (x != NULL) continue;
                break;
            }
            /* -Qnew is in effect:  fall through to
               BINARY_TRUE_DIVIDE */
"""
code[27]="""            w = POP();
            v = TOP();
            x = PyNumber_TrueDivide(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[26]="""            w = POP();
            v = TOP();
            x = PyNumber_FloorDivide(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[22]="""            w = POP();
            v = TOP();
            if (PyString_CheckExact(v))
                x = PyString_Format(v, w);
            else
                x = PyNumber_Remainder(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;


"""
code[148]="""            w = POP();
            v = TOP();
            if (PyString_CheckExact(v))
                x = PyString_Format(v, w);
            else
                x = PyNumber_Remainder(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            x = GETITEM(consts, oparg);
            Py_INCREF(x);
            PUSH(x);
            goto fast_next_opcode;



"""
code[23]="""            w = POP();
            v = TOP();
            if (PyInt_CheckExact(v) && PyInt_CheckExact(w)) {
                /* INLINE: int + int */
                register long a, b, i;
                a = PyInt_AS_LONG(v);
                b = PyInt_AS_LONG(w);
                /* cast to avoid undefined behaviour
                   on overflow */
                i = (long)((unsigned long)a + b);
                if ((i^a) < 0 && (i^b) < 0)
                    goto slow_add;
                x = PyInt_FromLong(i);
            }
            else if (PyString_CheckExact(v) &&
                     PyString_CheckExact(w)) {
                x = string_concatenate(v, w, f, next_instr);
                /* string_concatenate consumed the ref to v */
                goto skip_decref_vx;
            }
            else {
              slow_add:
                x = PyNumber_Add(v, w);
            }
            Py_DECREF(v);
          skip_decref_vx:
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[24]="""            w = POP();
            v = TOP();
            if (PyInt_CheckExact(v) && PyInt_CheckExact(w)) {
                /* INLINE: int - int */
                register long a, b, i;
                a = PyInt_AS_LONG(v);
                b = PyInt_AS_LONG(w);
                /* cast to avoid undefined behaviour
                   on overflow */
                i = (long)((unsigned long)a - b);
                if ((i^a) < 0 && (i^~b) < 0)
                    goto slow_sub;
                x = PyInt_FromLong(i);
            }
            else {
                x = PyNumber_Subtract(v, w);
            }
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[25]="""            w = POP();
            v = TOP();
            if (PyList_CheckExact(v) && PyInt_CheckExact(w)) {
                /* INLINE: list[int] */
                Py_ssize_t i = PyInt_AsSsize_t(w);
                if (i < 0)
                    i += PyList_GET_SIZE(v);
                if (i >= 0 && i < PyList_GET_SIZE(v)) {
                    x = PyList_GET_ITEM(v, i);
                    Py_INCREF(x);
                }
                else
                    goto slow_get;
            }
            else
              slow_get:
                x = PyObject_GetItem(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[62]="""            w = POP();
            v = TOP();
            x = PyNumber_Lshift(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[63]="""            w = POP();
            v = TOP();
            x = PyNumber_Rshift(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[64]="""            w = POP();
            v = TOP();
            x = PyNumber_And(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[65]="""            w = POP();
            v = TOP();
            x = PyNumber_Xor(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[66]="""            w = POP();
            v = TOP();
            x = PyNumber_Or(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[94]="""            w = POP();
            v = PEEK(oparg);
            err = PyList_Append(v, w);
            Py_DECREF(w);
            if (err == 0) {
                PREDICT(JUMP_ABSOLUTE);
                continue;
            }
            break;

"""
code[146]="""            w = POP();
            v = stack_pointer[-oparg];
            err = PySet_Add(v, w);
            Py_DECREF(w);
            if (err == 0) {
                PREDICT(JUMP_ABSOLUTE);
                continue;
            }
            break;

"""
code[67]="""            w = POP();
            v = TOP();
            x = PyNumber_InPlacePower(v, w, Py_None);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[57]="""            w = POP();
            v = TOP();
            x = PyNumber_InPlaceMultiply(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[58]="""            if (!_Py_QnewFlag) {
                w = POP();
                v = TOP();
                x = PyNumber_InPlaceDivide(v, w);
                Py_DECREF(v);
                Py_DECREF(w);
                SET_TOP(x);
                if (x != NULL) continue;
                break;
            }
            /* -Qnew is in effect:  fall through to
               INPLACE_TRUE_DIVIDE */
"""
code[29]="""            w = POP();
            v = TOP();
            x = PyNumber_InPlaceTrueDivide(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[28]="""            w = POP();
            v = TOP();
            x = PyNumber_InPlaceFloorDivide(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[59]="""            w = POP();
            v = TOP();
            x = PyNumber_InPlaceRemainder(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[55]="""            w = POP();
            v = TOP();
            if (PyInt_CheckExact(v) && PyInt_CheckExact(w)) {
                /* INLINE: int + int */
                register long a, b, i;
                a = PyInt_AS_LONG(v);
                b = PyInt_AS_LONG(w);
                i = a + b;
                if ((i^a) < 0 && (i^b) < 0)
                    goto slow_iadd;
                x = PyInt_FromLong(i);
            }
            else if (PyString_CheckExact(v) &&
                     PyString_CheckExact(w)) {
                x = string_concatenate(v, w, f, next_instr);
                /* string_concatenate consumed the ref to v */
                goto skip_decref_v;
            }
            else {
              slow_iadd:
                x = PyNumber_InPlaceAdd(v, w);
            }
            Py_DECREF(v);
          skip_decref_v:
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[56]="""            w = POP();
            v = TOP();
            if (PyInt_CheckExact(v) && PyInt_CheckExact(w)) {
                /* INLINE: int - int */
                register long a, b, i;
                a = PyInt_AS_LONG(v);
                b = PyInt_AS_LONG(w);
                i = a - b;
                if ((i^a) < 0 && (i^~b) < 0)
                    goto slow_isub;
                x = PyInt_FromLong(i);
            }
            else {
                x = PyNumber_InPlaceSubtract(v, w);
            }
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[75]="""            w = POP();
            v = TOP();
            x = PyNumber_InPlaceLshift(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[76]="""            w = POP();
            v = TOP();
            x = PyNumber_InPlaceRshift(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[77]="""            w = POP();
            v = TOP();
            x = PyNumber_InPlaceAnd(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[78]="""            w = POP();
            v = TOP();
            x = PyNumber_InPlaceXor(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[79]="""            w = POP();
            v = TOP();
            x = PyNumber_InPlaceOr(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[30]=""""""
code[31]=""""""
code[32]=""""""
code[33]="""            if ((opcode-SLICE) & 2)
                w = POP();
            else
                w = NULL;
            if ((opcode-SLICE) & 1)
                v = POP();
            else
                v = NULL;
            u = TOP();
            x = apply_slice(u, v, w);
            Py_DECREF(u);
            Py_XDECREF(v);
            Py_XDECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[40]=""""""
code[41]=""""""
code[42]=""""""
code[43]="""            if ((opcode-STORE_SLICE) & 2)
                w = POP();
            else
                w = NULL;
            if ((opcode-STORE_SLICE) & 1)
                v = POP();
            else
                v = NULL;
            u = POP();
            t = POP();
            err = assign_slice(u, v, w, t); /* u[v:w] = t */
            Py_DECREF(t);
            Py_DECREF(u);
            Py_XDECREF(v);
            Py_XDECREF(w);
            if (err == 0) continue;
            break;

"""
code[50]=""""""
code[51]=""""""
code[52]=""""""
code[53]="""            if ((opcode-DELETE_SLICE) & 2)
                w = POP();
            else
                w = NULL;
            if ((opcode-DELETE_SLICE) & 1)
                v = POP();
            else
                v = NULL;
            u = POP();
            err = assign_slice(u, v, w, (PyObject *)NULL);
                                            /* del u[v:w] */
            Py_DECREF(u);
            Py_XDECREF(v);
            Py_XDECREF(w);
            if (err == 0) continue;
            break;

"""
code[60]="""            w = TOP();
            v = SECOND();
            u = THIRD();
            STACKADJ(-3);
            /* v[w] = u */
            err = PyObject_SetItem(v, w, u);
            Py_DECREF(u);
            Py_DECREF(v);
            Py_DECREF(w);
            if (err == 0) continue;
            break;

"""
code[61]="""            w = TOP();
            v = SECOND();
            STACKADJ(-2);
            /* del v[w] */
            err = PyObject_DelItem(v, w);
            Py_DECREF(v);
            Py_DECREF(w);
            if (err == 0) continue;
            break;

"""
code[70]="""            v = POP();
            w = PySys_GetObject("displayhook");
            if (w == NULL) {
                PyErr_SetString(PyExc_RuntimeError,
                                "lost sys.displayhook");
                err = -1;
                x = NULL;
            }
            if (err == 0) {
                x = PyTuple_Pack(1, v);
                if (x == NULL)
                    err = -1;
            }
            if (err == 0) {
                w = PyEval_CallObject(w, x);
                Py_XDECREF(w);
                if (w == NULL)
                    err = -1;
            }
            Py_DECREF(v);
            Py_XDECREF(x);
            break;

"""
code[73]="""            w = stream = POP();
            /* fall through to PRINT_ITEM */

"""
code[71]="""            v = POP();
            if (stream == NULL || stream == Py_None) {
                w = PySys_GetObject("stdout");
                if (w == NULL) {
                    PyErr_SetString(PyExc_RuntimeError,
                                    "lost sys.stdout");
                    err = -1;
                }
            }
            /* PyFile_SoftSpace() can exececute arbitrary code
               if sys.stdout is an instance with a __getattr__.
               If __getattr__ raises an exception, w will
               be freed, so we need to prevent that temporarily. */
            Py_XINCREF(w);
            if (w != NULL && PyFile_SoftSpace(w, 0))
                err = PyFile_WriteString(" ", w);
            if (err == 0)
                err = PyFile_WriteObject(v, w, Py_PRINT_RAW);
            if (err == 0) {
                /* XXX move into writeobject() ? */
                if (PyString_Check(v)) {
                    char *s = PyString_AS_STRING(v);
                    Py_ssize_t len = PyString_GET_SIZE(v);
                    if (len == 0 ||
                        !isspace(Py_CHARMASK(s[len-1])) ||
                        s[len-1] == ' ')
                        PyFile_SoftSpace(w, 1);
                }
#ifdef Py_USING_UNICODE
                else if (PyUnicode_Check(v)) {
                    Py_UNICODE *s = PyUnicode_AS_UNICODE(v);
                    Py_ssize_t len = PyUnicode_GET_SIZE(v);
                    if (len == 0 ||
                        !Py_UNICODE_ISSPACE(s[len-1]) ||
                        s[len-1] == ' ')
                        PyFile_SoftSpace(w, 1);
                }
#endif
                else
                    PyFile_SoftSpace(w, 1);
            }
            Py_XDECREF(w);
            Py_DECREF(v);
            Py_XDECREF(stream);
            stream = NULL;
            if (err == 0)
                continue;
            break;

"""
code[74]="""            w = stream = POP();
            /* fall through to PRINT_NEWLINE */

"""
code[72]="""            if (stream == NULL || stream == Py_None) {
                w = PySys_GetObject("stdout");
                if (w == NULL) {
                    PyErr_SetString(PyExc_RuntimeError,
                                    "lost sys.stdout");
                    why = WHY_EXCEPTION;
                }
            }
            if (w != NULL) {
                /* w.write() may replace sys.stdout, so we
                 * have to keep our reference to it */
                Py_INCREF(w);
                err = PyFile_WriteString("\n", w);
                if (err == 0)
                    PyFile_SoftSpace(w, 0);
                Py_DECREF(w);
            }
            Py_XDECREF(stream);
            stream = NULL;
            break;


#ifdef CASE_TOO_BIG
        default: switch (opcode) {
#endif
"""
code[130]="""            u = v = w = NULL;
            switch (oparg) {
                /* Fallthrough */
                v = POP(); /* value */
                /* Fallthrough */
                w = POP(); /* exc */
                why = do_raise(w, v, u);
                break;
            default:
                PyErr_SetString(PyExc_SystemError,
                           "bad RAISE_VARARGS oparg");
                why = WHY_EXCEPTION;
                break;
            }
            break;

"""
code[82]="""            if ((x = f->f_locals) != NULL) {
                Py_INCREF(x);
                PUSH(x);
                continue;
            }
            PyErr_SetString(PyExc_SystemError, "no locals");
            break;

"""
code[83]="""            retval = POP();
            why = WHY_RETURN;
            goto fast_block_end;

"""
code[86]="""            retval = POP();
            f->f_stacktop = stack_pointer;
            why = WHY_YIELD;
            goto fast_yield;

"""
code[85]="""            w = TOP();
            v = SECOND();
            u = THIRD();
            STACKADJ(-3);
            READ_TIMESTAMP(intr0);
            err = exec_statement(f, u, v, w);
            READ_TIMESTAMP(intr1);
            Py_DECREF(u);
            Py_DECREF(v);
            Py_DECREF(w);
            break;

"""
code[87]="""            {
                PyTryBlock *b = PyFrame_BlockPop(f);
                while (STACK_LEVEL() > b->b_level) {
                    v = POP();
                    Py_DECREF(v);
                }
            }
            continue;

        PREDICTED(END_FINALLY);
"""
code[88]="""            v = POP();
            if (PyInt_Check(v)) {
                why = (enum why_code) PyInt_AS_LONG(v);
                assert(why != WHY_YIELD);
                if (why == WHY_RETURN ||
                    why == WHY_CONTINUE)
                    retval = POP();
            }
            else if (PyExceptionClass_Check(v) ||
                     PyString_Check(v)) {
                w = POP();
                u = POP();
                PyErr_Restore(v, w, u);
                why = WHY_RERAISE;
                break;
            }
            else if (v != Py_None) {
                PyErr_SetString(PyExc_SystemError,
                    "'finally' pops bad exception");
                why = WHY_EXCEPTION;
            }
            Py_DECREF(v);
            break;

"""
code[89]="""            u = TOP();
            v = SECOND();
            w = THIRD();
            STACKADJ(-2);
            x = build_class(u, v, w);
            SET_TOP(x);
            Py_DECREF(u);
            Py_DECREF(v);
            Py_DECREF(w);
            break;

"""
code[90]="""            w = GETITEM(names, oparg);
            v = POP();
            if ((x = f->f_locals) != NULL) {
                if (PyDict_CheckExact(x))
                    err = PyDict_SetItem(x, w, v);
                else
                    err = PyObject_SetItem(x, w, v);
                Py_DECREF(v);
                if (err == 0) continue;
                break;
            }
            PyErr_Format(PyExc_SystemError,
                         "no locals found when storing %s",
                         PyObject_REPR(w));
            break;

"""
code[91]="""            w = GETITEM(names, oparg);
            if ((x = f->f_locals) != NULL) {
                if ((err = PyObject_DelItem(x, w)) != 0)
                    format_exc_check_arg(PyExc_NameError,
                                         NAME_ERROR_MSG,
                                         w);
                break;
            }
            PyErr_Format(PyExc_SystemError,
                         "no locals when deleting %s",
                         PyObject_REPR(w));
            break;

"""
code[92]="""            v = POP();
            if (PyTuple_CheckExact(v) &&
                PyTuple_GET_SIZE(v) == oparg) {
                PyObject **items = \
                    ((PyTupleObject *)v)->ob_item;
                while (oparg--) {
                    w = items[oparg];
                    Py_INCREF(w);
                    PUSH(w);
                }
                Py_DECREF(v);
                continue;
            } else if (PyList_CheckExact(v) &&
                       PyList_GET_SIZE(v) == oparg) {
                PyObject **items = \
                    ((PyListObject *)v)->ob_item;
                while (oparg--) {
                    w = items[oparg];
                    Py_INCREF(w);
                    PUSH(w);
                }
            } else if (unpack_iterable(v, oparg,
                                       stack_pointer + oparg)) {
                STACKADJ(oparg);
            } else {
                /* unpack_iterable() raised an exception */
                why = WHY_EXCEPTION;
            }
            Py_DECREF(v);
            break;

"""
code[95]="""            w = GETITEM(names, oparg);
            v = TOP();
            u = SECOND();
            STACKADJ(-2);
            err = PyObject_SetAttr(v, w, u); /* v.w = u */
            Py_DECREF(v);
            Py_DECREF(u);
            if (err == 0) continue;
            break;

"""
code[96]="""            w = GETITEM(names, oparg);
            v = POP();
            err = PyObject_SetAttr(v, w, (PyObject *)NULL);
                                            /* del v.w */
            Py_DECREF(v);
            break;

"""
code[97]="""            w = GETITEM(names, oparg);
            v = POP();
            err = PyDict_SetItem(f->f_globals, w, v);
            Py_DECREF(v);
            if (err == 0) continue;
            break;

"""
code[98]="""            w = GETITEM(names, oparg);
            if ((err = PyDict_DelItem(f->f_globals, w)) != 0)
                format_exc_check_arg(
                    PyExc_NameError, GLOBAL_NAME_ERROR_MSG, w);
            break;

"""
code[101]="""            w = GETITEM(names, oparg);
            if ((v = f->f_locals) == NULL) {
                PyErr_Format(PyExc_SystemError,
                             "no locals when loading %s",
                             PyObject_REPR(w));
                why = WHY_EXCEPTION;
                break;
            }
            if (PyDict_CheckExact(v)) {
                x = PyDict_GetItem(v, w);
                Py_XINCREF(x);
            }
            else {
                x = PyObject_GetItem(v, w);
                if (x == NULL && PyErr_Occurred()) {
                    if (!PyErr_ExceptionMatches(
                                    PyExc_KeyError))
                        break;
                    PyErr_Clear();
                }
            }
            if (x == NULL) {
                x = PyDict_GetItem(f->f_globals, w);
                if (x == NULL) {
                    x = PyDict_GetItem(f->f_builtins, w);
                    if (x == NULL) {
                        format_exc_check_arg(
                                    PyExc_NameError,
                                    NAME_ERROR_MSG, w);
                        break;
                    }
                }
                Py_INCREF(x);
            }
            PUSH(x);
            continue;

"""
code[116]="""            w = GETITEM(names, oparg);
            if (PyString_CheckExact(w)) {
                /* Inline the PyDict_GetItem() calls.
                   WARNING: this is an extreme speed hack.
                   Do not try this at home. */
                long hash = ((PyStringObject *)w)->ob_shash;
                if (hash != -1) {
                    PyDictObject *d;
                    PyDictEntry *e;
                    d = (PyDictObject *)(f->f_globals);
                    e = d->ma_lookup(d, w, hash);
                    if (e == NULL) {
                        x = NULL;
                        break;
                    }
                    x = e->me_value;
                    if (x != NULL) {
                        Py_INCREF(x);
                        PUSH(x);
                        continue;
                    }
                    d = (PyDictObject *)(f->f_builtins);
                    e = d->ma_lookup(d, w, hash);
                    if (e == NULL) {
                        x = NULL;
                        break;
                    }
                    x = e->me_value;
                    if (x != NULL) {
                        Py_INCREF(x);
                        PUSH(x);
                        continue;
                    }
                    goto load_global_error;
                }
            }
            /* This is the un-inlined version of the code above */
            x = PyDict_GetItem(f->f_globals, w);
            if (x == NULL) {
                x = PyDict_GetItem(f->f_builtins, w);
                if (x == NULL) {
                    format_exc_check_arg(
                                PyExc_NameError,
                                GLOBAL_NAME_ERROR_MSG, w);
                    break;
                }
            }
            Py_INCREF(x);
            PUSH(x);
            continue;

"""
code[126]="""            x = GETLOCAL(oparg);
            if (x != NULL) {
                SETLOCAL(oparg, NULL);
                continue;
            }
            format_exc_check_arg(
                PyExc_UnboundLocalError,
                UNBOUNDLOCAL_ERROR_MSG,
                PyTuple_GetItem(co->co_varnames, oparg)
                );
            break;

"""
code[135]="""            x = freevars[oparg];
            Py_INCREF(x);
            PUSH(x);
            if (x != NULL) continue;
            break;

"""
code[136]="""            x = freevars[oparg];
            w = PyCell_Get(x);
            if (w != NULL) {
                PUSH(w);
                continue;
            }
            err = -1;
            /* Don't stomp existing exception */
            if (PyErr_Occurred())
                break;
            if (oparg < PyTuple_GET_SIZE(co->co_cellvars)) {
                v = PyTuple_GET_ITEM(co->co_cellvars,
                                     oparg);
                format_exc_check_arg(
                       PyExc_UnboundLocalError,
                       UNBOUNDLOCAL_ERROR_MSG,
                       v);
            } else {
                v = PyTuple_GET_ITEM(co->co_freevars, oparg -
                    PyTuple_GET_SIZE(co->co_cellvars));
                format_exc_check_arg(PyExc_NameError,
                                     UNBOUNDFREE_ERROR_MSG, v);
            }
            break;

"""
code[137]="""            w = POP();
            x = freevars[oparg];
            PyCell_Set(x, w);
            Py_DECREF(w);
            continue;

"""
code[102]="""            x = PyTuple_New(oparg);
            if (x != NULL) {
                for (; --oparg >= 0;) {
                    w = POP();
                    PyTuple_SET_ITEM(x, oparg, w);
                }
                PUSH(x);
                continue;
            }
            break;

"""
code[103]="""            x =  PyList_New(oparg);
            if (x != NULL) {
                for (; --oparg >= 0;) {
                    w = POP();
                    PyList_SET_ITEM(x, oparg, w);
                }
                PUSH(x);
                continue;
            }
            break;

"""
code[104]="""            x = PySet_New(NULL);
            if (x != NULL) {
                for (; --oparg >= 0;) {
                    w = POP();
                    if (err == 0)
                        err = PySet_Add(x, w);
                    Py_DECREF(w);
                }
                if (err != 0) {
                    Py_DECREF(x);
                    break;
                }
                PUSH(x);
                continue;
            }
            break;


"""
code[105]="""            x = _PyDict_NewPresized((Py_ssize_t)oparg);
            PUSH(x);
            if (x != NULL) continue;
            break;

"""
code[54]="""            w = TOP();     /* key */
            u = SECOND();  /* value */
            v = THIRD();   /* dict */
            STACKADJ(-2);
            assert (PyDict_CheckExact(v));
            err = PyDict_SetItem(v, w, u);  /* v[w] = u */
            Py_DECREF(u);
            Py_DECREF(w);
            if (err == 0) continue;
            break;

"""
code[147]="""            w = TOP();     /* key */
            u = SECOND();  /* value */
            STACKADJ(-2);
            v = stack_pointer[-oparg];  /* dict */
            assert (PyDict_CheckExact(v));
            err = PyDict_SetItem(v, w, u);  /* v[w] = u */
            Py_DECREF(u);
            Py_DECREF(w);
            if (err == 0) {
                PREDICT(JUMP_ABSOLUTE);
                continue;
            }
            break;

"""
code[106]="""            w = GETITEM(names, oparg);
            v = TOP();
            x = PyObject_GetAttr(v, w);
            Py_DECREF(v);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[107]="""            w = POP();
            v = TOP();
            if (PyInt_CheckExact(w) && PyInt_CheckExact(v)) {
                /* INLINE: cmp(int, int) */
                register long a, b;
                register int res;
                a = PyInt_AS_LONG(v);
                b = PyInt_AS_LONG(w);
                switch (oparg) {
"""
"""
"""
"""
"""
"""
"""
"""
                default: goto slow_compare;
                }
                x = res ? Py_True : Py_False;
                Py_INCREF(x);
            }
            else {
              slow_compare:
                x = cmp_outcome(oparg, v, w);
            }
            Py_DECREF(v);
            Py_DECREF(w);
            SET_TOP(x);
            if (x == NULL) break;
            PREDICT(POP_JUMP_IF_FALSE);
            PREDICT(POP_JUMP_IF_TRUE);
            continue;

"""
code[108]="""            w = GETITEM(names, oparg);
            x = PyDict_GetItemString(f->f_builtins, "__import__");
            if (x == NULL) {
                PyErr_SetString(PyExc_ImportError,
                                "__import__ not found");
                break;
            }
            Py_INCREF(x);
            v = POP();
            u = TOP();
            if (PyInt_AsLong(u) != -1 || PyErr_Occurred())
                w = PyTuple_Pack(5,
                            w,
                            f->f_globals,
                            f->f_locals == NULL ?
                                  Py_None : f->f_locals,
                            v,
                            u);
            else
                w = PyTuple_Pack(4,
                            w,
                            f->f_globals,
                            f->f_locals == NULL ?
                                  Py_None : f->f_locals,
                            v);
            Py_DECREF(v);
            Py_DECREF(u);
            if (w == NULL) {
                u = POP();
                Py_DECREF(x);
                x = NULL;
                break;
            }
            READ_TIMESTAMP(intr0);
            v = x;
            x = PyEval_CallObject(v, w);
            Py_DECREF(v);
            READ_TIMESTAMP(intr1);
            Py_DECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[84]="""            v = POP();
            PyFrame_FastToLocals(f);
            if ((x = f->f_locals) == NULL) {
                PyErr_SetString(PyExc_SystemError,
                    "no locals found during 'import *'");
                break;
            }
            READ_TIMESTAMP(intr0);
            err = import_all_from(x, v);
            READ_TIMESTAMP(intr1);
            PyFrame_LocalsToFast(f, 0);
            Py_DECREF(v);
            if (err == 0) continue;
            break;

"""
code[109]="""            w = GETITEM(names, oparg);
            v = TOP();
            READ_TIMESTAMP(intr0);
            x = import_from(v, w);
            READ_TIMESTAMP(intr1);
            PUSH(x);
            if (x != NULL) continue;
            break;

"""
code[110]="""            JUMPBY(oparg);
            goto fast_next_opcode;

"""
code[114]="""            w = POP();
            if (w == Py_True) {
                Py_DECREF(w);
                goto fast_next_opcode;
            }
            if (w == Py_False) {
                Py_DECREF(w);
                JUMPTO(oparg);
                goto fast_next_opcode;
            }
            err = PyObject_IsTrue(w);
            Py_DECREF(w);
            if (err > 0)
                err = 0;
            else if (err == 0)
                JUMPTO(oparg);
            else
                break;
            continue;

"""
code[115]="""            w = POP();
            if (w == Py_False) {
                Py_DECREF(w);
                goto fast_next_opcode;
            }
            if (w == Py_True) {
                Py_DECREF(w);
                JUMPTO(oparg);
                goto fast_next_opcode;
            }
            err = PyObject_IsTrue(w);
            Py_DECREF(w);
            if (err > 0) {
                err = 0;
                JUMPTO(oparg);
            }
            else if (err == 0)
                ;
            else
                break;
            continue;

"""
code[111]="""            w = TOP();
            if (w == Py_True) {
                STACKADJ(-1);
                Py_DECREF(w);
                goto fast_next_opcode;
            }
            if (w == Py_False) {
                JUMPTO(oparg);
                goto fast_next_opcode;
            }
            err = PyObject_IsTrue(w);
            if (err > 0) {
                STACKADJ(-1);
                Py_DECREF(w);
                err = 0;
            }
            else if (err == 0)
                JUMPTO(oparg);
            else
                break;
            continue;

"""
code[112]="""            w = TOP();
            if (w == Py_False) {
                STACKADJ(-1);
                Py_DECREF(w);
                goto fast_next_opcode;
            }
            if (w == Py_True) {
                JUMPTO(oparg);
                goto fast_next_opcode;
            }
            err = PyObject_IsTrue(w);
            if (err > 0) {
                err = 0;
                JUMPTO(oparg);
            }
            else if (err == 0) {
                STACKADJ(-1);
                Py_DECREF(w);
            }
            else
                break;
            continue;

"""
code[113]="""            JUMPTO(oparg);
#if FAST_LOOPS
            /* Enabling this path speeds-up all while and for-loops by bypassing
               the per-loop checks for signals.  By default, this should be turned-off
               because it prevents detection of a control-break in tight loops like
               "while 1: pass".  Compile with this option turned-on when you need
               the speed-up and do not need break checking inside tight loops (ones
               that contain only instructions ending with goto fast_next_opcode).
            */
            goto fast_next_opcode;
#else
            continue;
#endif

"""
code[68]="""            /* before: [obj]; after [getiter(obj)] */
            v = TOP();
            x = PyObject_GetIter(v);
            Py_DECREF(v);
            if (x != NULL) {
                SET_TOP(x);
                PREDICT(FOR_ITER);
                continue;
            }
            STACKADJ(-1);
            break;

"""
code[93]="""            /* before: [iter]; after: [iter, iter()] *or* [] */
            v = TOP();
            x = (*v->ob_type->tp_iternext)(v);
            if (x != NULL) {
                PUSH(x);
                PREDICT(STORE_FAST);
                PREDICT(UNPACK_SEQUENCE);
                continue;
            }
            if (PyErr_Occurred()) {
                if (!PyErr_ExceptionMatches(
                                PyExc_StopIteration))
                    break;
                PyErr_Clear();
            }
            /* iterator ended normally */
            x = v = POP();
            Py_DECREF(v);
            JUMPBY(oparg);
            continue;

"""
code[80]="""            why = WHY_BREAK;
            goto fast_block_end;

"""
code[119]="""            retval = PyInt_FromLong(oparg);
            if (!retval) {
                x = NULL;
                break;
            }
            why = WHY_CONTINUE;
            goto fast_block_end;

"""
code[120]=""""""
code[121]=""""""
code[122]="""            /* NOTE: If you add any new block-setup opcodes that
               are not try/except/finally handlers, you may need
               to update the PyGen_NeedsFinalizing() function.
               */

            PyFrame_BlockSetup(f, opcode, INSTR_OFFSET() + oparg,
                               STACK_LEVEL());
            continue;

"""
code[143]="""        {
            static PyObject *exit, *enter;
            w = TOP();
            x = special_lookup(w, "__exit__", &exit);
            if (!x)
                break;
            SET_TOP(x);
            u = special_lookup(w, "__enter__", &enter);
            Py_DECREF(w);
            if (!u) {
                x = NULL;
                break;
            }
            x = PyObject_CallFunctionObjArgs(u, NULL);
            Py_DECREF(u);
            if (!x)
                break;
            /* Setup a finally block (SETUP_WITH as a block is
               equivalent to SETUP_FINALLY except it normalizes
               the exception) before pushing the result of
               __enter__ on the stack. */
            PyFrame_BlockSetup(f, SETUP_WITH, INSTR_OFFSET() + oparg,
                               STACK_LEVEL());

            PUSH(x);
            continue;
        }

"""
code[81]="""        {
            /* At the top of the stack are 1-3 values indicating
               how/why we entered the finally clause:
               - TOP = None
               - (TOP, SECOND) = (WHY_{RETURN,CONTINUE}), retval
               - TOP = WHY_*; no retval below it
               - (TOP, SECOND, THIRD) = exc_info()
               Below them is EXIT, the context.__exit__ bound method.
               In the last case, we must call
                 EXIT(TOP, SECOND, THIRD)
               otherwise we must call
                 EXIT(None, None, None)

               In all cases, we remove EXIT from the stack, leaving
               the rest in the same order.

               In addition, if the stack represents an exception,
               *and* the function call returns a 'true' value, we
               "zap" this information, to prevent END_FINALLY from
               re-raising the exception.  (But non-local gotos
               should still be resumed.)
            */

            PyObject *exit_func;

            u = POP();
            if (u == Py_None) {
                exit_func = TOP();
                SET_TOP(u);
                v = w = Py_None;
            }
            else if (PyInt_Check(u)) {
                switch(PyInt_AS_LONG(u)) {
"""
"""
                    /* Retval in TOP. */
                    exit_func = SECOND();
                    SET_SECOND(TOP());
                    SET_TOP(u);
                    break;
                default:
                    exit_func = TOP();
                    SET_TOP(u);
                    break;
                }
                u = v = w = Py_None;
            }
            else {
                v = TOP();
                w = SECOND();
                exit_func = THIRD();
                SET_TOP(u);
                SET_SECOND(v);
                SET_THIRD(w);
            }
            /* XXX Not the fastest way to call it... */
            x = PyObject_CallFunctionObjArgs(exit_func, u, v, w,
                                             NULL);
            Py_DECREF(exit_func);
            if (x == NULL)
                break; /* Go to error exit */

            if (u != Py_None)
                err = PyObject_IsTrue(x);
            else
                err = 0;
            Py_DECREF(x);

            if (err < 0)
                break; /* Go to error exit */
            else if (err > 0) {
                err = 0;
                /* There was an exception and a true return */
                STACKADJ(-2);
                Py_INCREF(Py_None);
                SET_TOP(Py_None);
                Py_DECREF(u);
                Py_DECREF(v);
                Py_DECREF(w);
            } else {
                /* The stack was rearranged to remove EXIT
                   above. Let END_FINALLY do its thing */
            }
            PREDICT(END_FINALLY);
            break;
        }

"""
code[131]="""        {
            PyObject **sp;
            PCALL(PCALL_ALL);
            sp = stack_pointer;
#ifdef WITH_TSC
            x = call_function(&sp, oparg, &intr0, &intr1);
#else
            x = call_function(&sp, oparg);
#endif
            stack_pointer = sp;
            PUSH(x);
            if (x != NULL)
                continue;
            break;
        }

"""
code[140]=""""""
code[141]=""""""
code[142]="""        {
            int na = oparg & 0xff;
            int nk = (oparg>>8) & 0xff;
            int flags = (opcode - CALL_FUNCTION) & 3;
            int n = na + 2 * nk;
            PyObject **pfunc, *func, **sp;
            PCALL(PCALL_ALL);
            if (flags & CALL_FLAG_VAR)
                n++;
            if (flags & CALL_FLAG_KW)
                n++;
            pfunc = stack_pointer - n - 1;
            func = *pfunc;

            if (PyMethod_Check(func)
                && PyMethod_GET_SELF(func) != NULL) {
                PyObject *self = PyMethod_GET_SELF(func);
                Py_INCREF(self);
                func = PyMethod_GET_FUNCTION(func);
                Py_INCREF(func);
                Py_DECREF(*pfunc);
                *pfunc = self;
                na++;
            } else
                Py_INCREF(func);
            sp = stack_pointer;
            READ_TIMESTAMP(intr0);
            x = ext_do_call(func, &sp, flags, na, nk);
            READ_TIMESTAMP(intr1);
            stack_pointer = sp;
            Py_DECREF(func);

            while (stack_pointer > pfunc) {
                w = POP();
                Py_DECREF(w);
            }
            PUSH(x);
            if (x != NULL)
                continue;
            break;
        }

"""
code[132]="""            v = POP(); /* code object */
            x = PyFunction_New(v, f->f_globals);
            Py_DECREF(v);
            /* XXX Maybe this should be a separate opcode? */
            if (x != NULL && oparg > 0) {
                v = PyTuple_New(oparg);
                if (v == NULL) {
                    Py_DECREF(x);
                    x = NULL;
                    break;
                }
                while (--oparg >= 0) {
                    w = POP();
                    PyTuple_SET_ITEM(v, oparg, w);
                }
                err = PyFunction_SetDefaults(x, v);
                Py_DECREF(v);
            }
            PUSH(x);
            break;

"""
code[134]="""        {
            v = POP(); /* code object */
            x = PyFunction_New(v, f->f_globals);
            Py_DECREF(v);
            if (x != NULL) {
                v = POP();
                if (PyFunction_SetClosure(x, v) != 0) {
                    /* Can't happen unless bytecode is corrupt. */
                    why = WHY_EXCEPTION;
                }
                Py_DECREF(v);
            }
            if (x != NULL && oparg > 0) {
                v = PyTuple_New(oparg);
                if (v == NULL) {
                    Py_DECREF(x);
                    x = NULL;
                    break;
                }
                while (--oparg >= 0) {
                    w = POP();
                    PyTuple_SET_ITEM(v, oparg, w);
                }
                if (PyFunction_SetDefaults(x, v) != 0) {
                    /* Can't happen unless
                       PyFunction_SetDefaults changes. */
                    why = WHY_EXCEPTION;
                }
                Py_DECREF(v);
            }
            PUSH(x);
            break;
        }

"""
code[133]="""            if (oparg == 3)
                w = POP();
            else
                w = NULL;
            v = POP();
            u = TOP();
            x = PySlice_New(u, v, w);
            Py_DECREF(u);
            Py_DECREF(v);
            Py_XDECREF(w);
            SET_TOP(x);
            if (x != NULL) continue;
            break;

"""
code[145]="""            opcode = NEXTOP();
            oparg = oparg<<16 | NEXTARG();
            goto dispatch_opcode;


"""
