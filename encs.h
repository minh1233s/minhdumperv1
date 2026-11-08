#pragma once


#include <Windows.h>


template<typename T>
struct vmval1
{
private:
    T Storage;


public:
    operator const T() const
    {
        return (T)((uintptr_t)Storage - (uintptr_t)this);
    }


    void operator=(const T& Value)
    {
        Storage = (T)((uintptr_t)Value + (uintptr_t)this);
    }


    const T operator->() const
    {
        return operator const T();
    }


    T Get() const
    {
        return operator const T();
    }


    void Set(const T& Value)
    {
        operator=(Value);
    }
};


template<typename T>
struct vmval2
{
private:
    T Storage;


public:
    operator const T() const
    {
        return (T)((uintptr_t)this - (uintptr_t)Storage);
    }


    void operator=(const T& Value)
    {
        Storage = (T)((uintptr_t)this - (uintptr_t)Value);
    }


    const T operator->() const
    {
        return operator const T();
    }


    T Get() const
    {
        return operator const T();
    }


    void Set(const T& Value)
    {
        operator=(Value);
    }
};


template<typename T>
struct vmval3
{
private:
    T Storage;


public:
    operator const T() const
    {
        return (T)((uintptr_t)this ^ (uintptr_t)Storage);
    }


    void operator=(const T& Value)
    {
        Storage = (T)((uintptr_t)Value ^ (uintptr_t)this);
    }


    const T operator->() const
    {
        return operator const T();
    }


    T Get() const
    {
        return operator const T();
    }


    void Set(const T& Value)
    {
        operator=(Value);
    }
};


template<typename T>
struct vmval4
{
private:
    T Storage;


public:
    operator const T() const
    {
        return (T)((uintptr_t)this + (uintptr_t)Storage);
    }


    void operator=(const T& Value)
    {
        Storage = (T)((uintptr_t)Value - (uintptr_t)this);
    }


    const T operator->() const
    {
        return operator const T();
    }


    T Get() const
    {
        return operator const T();
    }


    void Set(const T& Value)
    {
        operator=(Value);
    }
};


#define CLOSURE_CONT_ENC vmval4
#define LSTATE_STACKSIZE_ENC vmval3
#define PROTO_ABSLINEINFO_ENC vmval4
#define PROTO_DEBUGINSN_ENC vmval3
#define PROTO_DEBUGNAME_ENC vmval3
#define PROTO_LINEINFO_ENC vmval3
#define PROTO_LOCVARS_ENC vmval3
#define PROTO_SOURCE_ENC vmval1
#define PROTO_TYPEINFO_ENC vmval3
#define PROTO_UPVALUES_ENC vmval2
#define PROTO_USERDATA_ENC vmval2
#define TSTRING_HASH_ENC vmval1
#define UDATA_META_ENC vmval1
