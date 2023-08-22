package com.psrom.registration.repository;

import com.psrom.registration.DTO.MemberDTO;
import org.springframework.stereotype.Repository;

@Repository
public class MemberRepository {
    public int save(MemberDTO memberDTO) {
        System.out.println("memberDTO= " + memberDTO);
        return 0;
    }
}
