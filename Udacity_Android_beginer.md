# Android Class for Beginner
> Udacity.com

> Support by Google

## Platform

Android Studio

## Layout

这是程序的外观展示， 书写在xml文件中，android studio提供动态可视化的工具，是全自动的。

### padding and margin

padding 是添加在子控件内部的，空来拓宽它的大小；margin必须是用在控件组(view group)里面，空来控制字面子控件其他控件的距离。
```
android:padding="8dp"
android:layout_margin="8dp"
```

### LinearLayout

这个layout组件是线性排布各个原件的，实例：
```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout   xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:orientation="vertical"
    android:id="@+id/activity_main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:paddingBottom="@dimen/activity_vertical_margin"
    android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    tools:context="com.example.lgy.test1.MainActivity"
    android:background="@android:color/background_dark">

    <ImageView
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"
        android:src="@android:drawable/ic_menu_today"/>
    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:background="#673ab7"
        android:layout_weight="0"
        android:text="You're invited!" />
    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:background="#673ab7"
        android:layout_weight="0"
        android:text="Bonfire at the beach" />
</LinearLayout>
```
上面中，“android:”是名字空间，最好都带上； layout_width/layout_height顾名思义是指控件的长宽。 硬编码的话用dp作为单位，就是说“200dp”这样，dp这个单位是相对的单位，在不同分辨率的屏幕上会有不同的大小，但是可以保持空间间固定的一个大小比例。

除了硬编码外，还可以用“match_parent”和“wrap_content”两种，前面的意思是大小和父控件一致，后面那个是就保持控件本本身的大小。

“layout_weight”这个的意思是如何占用屏幕剩余的空间，这是比例系数，如果设为0，那控件不占用任何多余的空间，layout_width/layout_weight设多少就是多少，如果不是0的话，根据比率去占用更多没用到的屏幕空间

属性定义中的“@”意思是调用android自带的资源。

“android:background”是控件背景颜色，“android:text”是控件内的文本内容，有的控件是没有的。

### RelativeLayout

控件默认是在左上角，通过相对关系来布置控件。

通过在子控件中添加这些属性来设置位置：
```
android:layout_alignParentLeft/Right/Top/Bottom="true"
```
这些位置属性默认是false。除此之外还有很多相对属性可以设置。

#### id
```
android:id="@+id/xxx"
```
上面的属性给一个控件定义id名， “@”是调用android内部的资源“+id”即是添加id，因为是第一次定义id所以需要用“+”，之后调用是不需要“+”号的。“xxx”是给予控件的id名。
使用的时候：
```
android:layout_toleftof="@id/xxx"
```
这是不需要“+”号，因为id已经定义了。
